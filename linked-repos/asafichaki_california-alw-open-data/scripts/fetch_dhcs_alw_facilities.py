#!/usr/bin/env python3
"""Fetch and normalize the public DHCS ALW participating-facilities layer."""

import csv
import json
import urllib.parse
import urllib.request
from pathlib import Path

SOURCE_URL = (
    "https://services7.arcgis.com/7MUwsS9z05YumJRZ/arcgis/rest/services/"
    "ALW_Assisted_Living_Facilities/FeatureServer/0/query"
)
SOURCE_ACCESS_DATE = "2026-07-18"
OUTPUT = Path(__file__).resolve().parents[1] / "california-alw-facilities-2026.csv"

FIELDS = [
    "provider_number",
    "legal_name",
    "business_name",
    "capacity_per_peu",
    "address",
    "address_2",
    "city",
    "county",
    "zip_code",
    "phone_number",
    "latitude",
    "longitude",
    "source_access_date",
]


def fetch_records():
    query = urllib.parse.urlencode(
        {
            "where": "1=1",
            "outFields": "*",
            "returnGeometry": "false",
            "f": "geojson",
        }
    )
    request = urllib.request.Request(
        f"{SOURCE_URL}?{query}",
        headers={"User-Agent": "California-Care-Compass-Open-Data/2026.1"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    return payload.get("features", [])


def normalize(feature):
    row = feature["properties"]
    capacity = row.get("Capacity_Per_PEU")
    # CountyName is the GIS-derived county and resolves 11 records where the
    # source's free-text County field conflicts with the mapped location.
    county = (row.get("CountyName") or row.get("County") or "")
    county = county.removesuffix(" County").strip().title()
    return {
        "provider_number": row.get("Number") or "",
        "legal_name": row.get("Legal_Name") or "",
        "business_name": row.get("Business_Name") or "",
        "capacity_per_peu": int(capacity) if capacity is not None else "",
        "address": row.get("Address") or "",
        "address_2": row.get("Address_2") or "",
        "city": row.get("City") or "",
        "county": county,
        "zip_code": row.get("Zip_Code") or "",
        "phone_number": row.get("Phone_Number") or "",
        "latitude": row.get("Latitude") or "",
        "longitude": row.get("Longitude") or "",
        "source_access_date": SOURCE_ACCESS_DATE,
    }


def main():
    records = [normalize(feature) for feature in fetch_records()]
    records.sort(
        key=lambda row: (
            row["county"].lower(),
            row["city"].lower(),
            row["business_name"].lower(),
            row["provider_number"],
        )
    )
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(records)
    print(f"Wrote {len(records)} records to {OUTPUT}")


if __name__ == "__main__":
    main()
