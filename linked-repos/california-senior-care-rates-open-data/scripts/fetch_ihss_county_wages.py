#!/usr/bin/env python3
"""
Fetch and normalize the CDSS IHSS Individual Provider (IP) county wage rates.

Reproducible, Python standard-library only. No third-party packages.
An .xlsx file is a ZIP of XML parts, so it is parsed with `zipfile` +
`xml.etree.ElementTree` rather than a spreadsheet library.

Source (California Department of Social Services, public domain):
  Page:  https://www.cdss.ca.gov/inforesources/ihss/county-ihss-wage-rates
  File:  https://www.cdss.ca.gov/Portals/9/IHSS/ip-cc-wages-by-county.xlsx

What this measures:
  The IHSS Individual Provider hourly WAGE set by each county and approved by
  CDSS. This is the wage paid to an in-home caregiver under the Medi-Cal In-Home
  Supportive Services program. It is NOT a private-pay home-care agency retail
  rate, and it is NOT an assisted-living or memory-care price.

Usage:
  python3 scripts/fetch_ihss_county_wages.py            # fetch live + write CSV/JSON
  python3 scripts/fetch_ihss_county_wages.py --dry-run  # fetch + print, write nothing
"""

import argparse
import csv
import datetime as dt
import io
import json
import os
import sys
import urllib.request
import zipfile
import xml.etree.ElementTree as ET

SOURCE_PAGE = "https://www.cdss.ca.gov/inforesources/ihss/county-ihss-wage-rates"
SOURCE_FILE = "https://www.cdss.ca.gov/Portals/9/IHSS/ip-cc-wages-by-county.xlsx"
# The workbook carries several historical tabs; this is the current IP wage tab.
TARGET_SHEET_NAME = "IP Effective 10-1-2026"

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

# Excel serial date epoch (1900 date system, with the well-known 1900 leap-year bug
# handled by the -2 offset used across the ecosystem).
EXCEL_EPOCH = dt.date(1899, 12, 30)


def _download(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "california-senior-care-rates-open-data/1.0 (+https://github.com/asafichaki)"
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def _col_to_index(cell_ref: str) -> int:
    """'B4' -> 1 (zero-based column index)."""
    letters = "".join(ch for ch in cell_ref if ch.isalpha())
    idx = 0
    for ch in letters:
        idx = idx * 26 + (ord(ch.upper()) - ord("A") + 1)
    return idx - 1


def _load_shared_strings(zf: zipfile.ZipFile) -> list:
    try:
        data = zf.read("xl/sharedStrings.xml")
    except KeyError:
        return []
    root = ET.fromstring(data)
    strings = []
    for si in root.findall("m:si", NS):
        # concatenate all text runs inside the shared-string item
        text = "".join(t.text or "" for t in si.iter("{%s}t" % NS["m"]))
        strings.append(text)
    return strings


def _sheet_path_for_name(zf: zipfile.ZipFile, name: str) -> str:
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rid = None
    for sheet in wb.find("m:sheets", NS).findall("m:sheet", NS):
        if sheet.get("name") == name:
            rid = sheet.get("{%s}id" % NS["r"])
            break
    if rid is None:
        raise SystemExit(f"Sheet named {name!r} not found in workbook.")
    target = None
    for rel in rels:
        if rel.get("Id") == rid:
            target = rel.get("Target")
            break
    if target is None:
        raise SystemExit(f"Relationship {rid} not found.")
    return "xl/" + target.lstrip("/")


def _excel_serial_to_date(serial: float):
    try:
        return (EXCEL_EPOCH + dt.timedelta(days=int(serial))).isoformat()
    except Exception:
        return None


def parse_workbook(xlsx_bytes: bytes) -> list:
    zf = zipfile.ZipFile(io.BytesIO(xlsx_bytes))
    shared = _load_shared_strings(zf)
    sheet_path = _sheet_path_for_name(zf, TARGET_SHEET_NAME)
    root = ET.fromstring(zf.read(sheet_path))
    sheet_data = root.find("m:sheetData", NS)

    records = []
    for row in sheet_data.findall("m:row", NS):
        cells = {}
        for c in row.findall("m:c", NS):
            ref = c.get("r")
            col = _col_to_index(ref)
            ctype = c.get("t")
            v = c.find("m:v", NS)
            if v is None or v.text is None:
                continue
            raw = v.text
            if ctype == "s":  # shared string
                cells[col] = shared[int(raw)]
            else:
                cells[col] = raw
        # Data rows: col 0 = county (string), col 1 = effective date (serial),
        # col 2 = wage (number). Header/title rows are skipped by these checks.
        county = cells.get(0)
        eff = cells.get(1)
        wage = cells.get(2)
        if not county or wage is None:
            continue
        county = county.strip()
        if county.upper() in ("COUNTY", "IHSS WAGES BY COUNTY"):
            continue
        try:
            wage_val = round(float(wage), 2)
        except ValueError:
            continue
        eff_date = _excel_serial_to_date(float(eff)) if eff else None
        records.append(
            {
                "county": county.title(),
                "hourly_wage_usd": wage_val,
                "wage_effective_date": eff_date,
            }
        )
    return records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="fetch + print, write nothing")
    ap.add_argument(
        "--out-dir",
        default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        help="directory to write CSV/JSON into (default: repo root)",
    )
    args = ap.parse_args()

    retrieved_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    print(f"Fetching {SOURCE_FILE} ...", file=sys.stderr)
    xlsx_bytes = _download(SOURCE_FILE)
    records = parse_workbook(xlsx_bytes)
    records.sort(key=lambda r: r["county"])

    if not records:
        raise SystemExit("No records parsed. Aborting (will not write an empty file).")

    wages = [r["hourly_wage_usd"] for r in records]
    lo = min(records, key=lambda r: r["hourly_wage_usd"])
    hi = max(records, key=lambda r: r["hourly_wage_usd"])
    srt = sorted(wages)
    n = len(srt)
    median = srt[n // 2] if n % 2 else round((srt[n // 2 - 1] + srt[n // 2]) / 2, 2)

    print(f"Parsed {len(records)} counties.", file=sys.stderr)
    print(f"  Lowest : {lo['county']} ${lo['hourly_wage_usd']}", file=sys.stderr)
    print(f"  Highest: {hi['county']} ${hi['hourly_wage_usd']}", file=sys.stderr)
    print(f"  Median : ${median}", file=sys.stderr)

    if args.dry_run:
        for r in records:
            print(r)
        return

    csv_path = os.path.join(args.out_dir, "california-ihss-county-wages-2026.csv")
    json_path = os.path.join(args.out_dir, "california-ihss-county-wages-2026.json")

    # Enrich each record with per-record provenance (the anti-mislabeling discipline).
    for r in records:
        r["measure_type"] = "provider_wage"
        r["is_private_pay_price"] = False
        r["source_name"] = "California Department of Social Services (CDSS), IHSS Individual Provider wage rates"
        r["source_file_url"] = SOURCE_FILE
        r["source_page_url"] = SOURCE_PAGE
        r["retrieved_at"] = retrieved_at
        r["produced_by"] = "scripts/fetch_ihss_county_wages.py"

    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "county",
                "hourly_wage_usd",
                "wage_effective_date",
                "measure_type",
                "is_private_pay_price",
                "source_name",
                "source_file_url",
                "source_page_url",
                "retrieved_at",
                "produced_by",
            ],
        )
        w.writeheader()
        w.writerows(records)

    dataset = {
        "dataset_name": "California IHSS Individual Provider County Wage Rates 2026",
        "version": "2026.1",
        "license": "CC BY 4.0",
        "publisher": "California Care Compass (https://californiacarecompass.com/)",
        "retrieved_at": retrieved_at,
        "measure_type": "provider_wage",
        "is_private_pay_price": False,
        "what_this_is": (
            "The hourly wage each California county pays an IHSS Individual Provider "
            "(in-home caregiver) under the Medi-Cal In-Home Supportive Services "
            "program, as approved by CDSS."
        ),
        "what_this_is_not": (
            "This is NOT a private-pay home-care agency retail rate, an assisted-living "
            "monthly price, a memory-care price, or a survey median. Do not present these "
            "wages as what a family pays out of pocket for private care."
        ),
        "sources": [
            {
                "name": "CDSS IHSS county wage rates page",
                "url": SOURCE_PAGE,
                "file_url": SOURCE_FILE,
                "sheet": TARGET_SHEET_NAME,
                "license": "Public domain (California state government)",
            }
        ],
        "definitions": {
            "hourly_wage_usd": "County-set IHSS Individual Provider hourly wage in US dollars.",
            "wage_effective_date": "Date the listed wage took effect (ISO 8601).",
            "monthly_fte_illustration_usd": (
                "ARITHMETIC ILLUSTRATION ONLY, not an observed cost: "
                "hourly_wage_usd x 173.33 (a nominal full-time month of 40h/week). "
                "Shown only to make the hourly figure intuitive; no family is billed this."
            ),
        },
        "summary": {
            "county_count": len(records),
            "lowest": {"county": lo["county"], "hourly_wage_usd": lo["hourly_wage_usd"]},
            "highest": {"county": hi["county"], "hourly_wage_usd": hi["hourly_wage_usd"]},
            "median_hourly_wage_usd": median,
            "spread_usd": round(hi["hourly_wage_usd"] - lo["hourly_wage_usd"], 2),
        },
        "records": [
            {
                "county": r["county"],
                "hourly_wage_usd": r["hourly_wage_usd"],
                "wage_effective_date": r["wage_effective_date"],
                "monthly_fte_illustration_usd": round(r["hourly_wage_usd"] * 173.33, 2),
                "measure_type": "provider_wage",
                "is_private_pay_price": False,
            }
            for r in records
        ],
    }
    with open(json_path, "w") as f:
        json.dump(dataset, f, indent=2)
        f.write("\n")

    print(f"Wrote {csv_path}", file=sys.stderr)
    print(f"Wrote {json_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
