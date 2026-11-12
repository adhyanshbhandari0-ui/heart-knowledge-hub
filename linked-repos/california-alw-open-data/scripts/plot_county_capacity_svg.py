#!/usr/bin/env python3
"""Create an accessible SVG bar chart from the county summary CSV."""

import csv
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "california-alw-county-tracker-2026.csv"
OUTPUT = ROOT / "examples" / "county-licensed-capacity.svg"


def main():
    rows = list(csv.DictReader(INPUT.open(encoding="utf-8")))
    rows.sort(key=lambda row: int(row["licensed_capacity_peu"]), reverse=True)
    width = 1000
    left = 170
    right = 100
    top = 100
    row_height = 38
    height = top + len(rows) * row_height + 90
    max_value = max(int(row["licensed_capacity_peu"]) for row in rows)
    plot_width = width - left - right

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Licensed Assisted Living Waiver capacity by California county</title>',
        '<desc id="desc">Horizontal bar chart showing licensed participant-enrollment-unit capacity in the 15 California counties with Assisted Living Waiver facilities.</desc>',
        '<rect width="100%" height="100%" fill="#fbfaf7"/>',
        '<text x="40" y="44" font-family="system-ui,sans-serif" font-size="26" font-weight="700" fill="#173d3f">California ALW licensed capacity by county</text>',
        '<text x="40" y="72" font-family="system-ui,sans-serif" font-size="15" fill="#52616b">Licensed PEU capacity is an approved ceiling, not a live vacancy count.</text>',
    ]
    for index, row in enumerate(rows):
        y = top + index * row_height
        value = int(row["licensed_capacity_peu"])
        bar_width = round(plot_width * value / max_value)
        county = html.escape(row["county"])
        parts.extend(
            [
                f'<text x="{left - 12}" y="{y + 20}" text-anchor="end" font-family="system-ui,sans-serif" font-size="14" fill="#26303a">{county}</text>',
                f'<rect x="{left}" y="{y + 5}" width="{bar_width}" height="22" rx="3" fill="#287d79"/>',
                f'<text x="{left + bar_width + 8}" y="{y + 21}" font-family="system-ui,sans-serif" font-size="13" fill="#26303a">{value:,}</text>',
            ]
        )
    parts.extend(
        [
            f'<text x="40" y="{height - 34}" font-family="system-ui,sans-serif" font-size="12" fill="#67737d">Source: California DHCS ALW participating-facilities GIS layer. California Care Compass, version 2026.1.</text>',
            '</svg>',
        ]
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
