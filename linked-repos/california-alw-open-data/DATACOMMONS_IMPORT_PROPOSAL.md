# Data Commons import proposal: California Assisted Living Waiver

Status: draft for Data Commons dataset-design review. No import or Data Commons endorsement is claimed.

## Dataset

- **Title:** California Assisted Living Waiver County Availability Tracker 2026
- **Publisher and curator:** California Care Compass
- **Human-readable dataset page:** https://californiacarecompass.com/data/california-alw-county-tracker-2026
- **Public repository:** https://github.com/asafichaki/california-alw-open-data
- **Versioned release:** https://github.com/asafichaki/california-alw-open-data/releases/tag/v2026.1
- **License:** CC BY 4.0
- **Coverage:** California; all 15 counties in which the Assisted Living Waiver operates

California Care Compass is a private-sector senior-care information and referral service. The underlying source records and statewide program totals are published by the California Department of Health Care Services (DHCS). County facility counts and licensed participant-enrollment-unit capacity are reproducible aggregates of the DHCS public GIS layer. The dataset does not estimate county waitlists or vacancies.

## Why this belongs in Data Commons

The dataset adds county-level access and capacity measures for a California Medicaid Home and Community-Based Services waiver. It supports comparisons between counties and combines clean geographic identifiers, explicit dates, open licensing, government provenance, facility-level source records, and a reproducible fetch script.

The proposed first import contains 32 observations:

- participating ALW facility count for 15 counties;
- total licensed participant-enrollment-unit capacity for the same 15 counties;
- statewide ALW enrollment; and
- statewide ALW waitlist count.

Licensed capacity is a regulatory ceiling, not a live vacancy count. DHCS publishes enrollment and waitlist only as statewide totals.

## Place mapping

County names map to existing Data Commons county DCIDs using five-digit Census FIPS codes. The mapping was checked against the [U.S. Census Bureau 2020 national county code file](https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt).

| County | Data Commons DCID |
|---|---|
| Alameda | `geoId/06001` |
| Contra Costa | `geoId/06013` |
| Fresno | `geoId/06019` |
| Kern | `geoId/06029` |
| Los Angeles | `geoId/06037` |
| Orange | `geoId/06059` |
| Riverside | `geoId/06065` |
| Sacramento | `geoId/06067` |
| San Bernardino | `geoId/06071` |
| San Diego | `geoId/06073` |
| San Francisco | `geoId/06075` |
| San Joaquin | `geoId/06077` |
| San Mateo | `geoId/06081` |
| Santa Clara | `geoId/06085` |
| Sonoma | `geoId/06097` |
| California | `geoId/06` |

## Proposed measures for design review

These are semantic descriptions, not final StatisticalVariable DCIDs. A search of the current Data Commons schema repository found related employment variables for NAICS assisted-living industries, but not the four program measures below. Final StatisticalVariables should be agreed with the Data Commons team before an import PR.

1. Number of facilities participating in California's Assisted Living Waiver.
2. Sum of licensed participant-enrollment-unit capacity at participating facilities.
3. Number of people enrolled in California's Assisted Living Waiver.
4. Number of people on California's Assisted Living Waiver waitlist.

Suggested observation dates:

- county facility and capacity snapshot: `2026-05-30` (source access and reproducible dataset version date);
- statewide enrollment and waitlist: `2025-12` (the period reported by DHCS).

## Source and artifact URLs

- DHCS participating-facilities GIS source: https://gis.dhcs.ca.gov/datasets/CADHCS::alw-assisted-living-facilities/about
- DHCS ALW program and reporting page: https://www.dhcs.ca.gov/services/long-term-care-alternatives-home-and-community-based-service-options/assisted-living-waiver/
- County CSV: https://github.com/asafichaki/california-alw-open-data/releases/download/v2026.1/california-alw-county-tracker-2026.csv
- Metadata JSON: https://github.com/asafichaki/california-alw-open-data/releases/download/v2026.1/california-alw-county-tracker-2026.json
- Facility-level CSV: https://github.com/asafichaki/california-alw-open-data/releases/download/v2026.1/california-alw-facilities-2026.csv
- Reproducible fetch script: https://github.com/asafichaki/california-alw-open-data/releases/download/v2026.1/fetch_dhcs_alw_facilities.py
- Frictionless Data Package metadata: https://github.com/asafichaki/california-alw-open-data/releases/download/v2026.1/datapackage.json

## Validation and caveats

- The county table has exactly 15 unique county rows and maps each row to one existing California county DCID.
- Facility totals are derived from 1,224 DHCS GIS records.
- Eleven source records disagree between a free-text county field and the GIS-derived county name; the reproducible pipeline uses the mapped county name and documents that choice.
- `licensed_capacity_peu` is not current availability or vacancy.
- No county-level enrollment or waitlist figures are asserted.
- The import should preserve DHCS as the underlying governmental source and California Care Compass as the curator of this open, normalized release.

## Requested next step

Please confirm whether Data Commons prefers a schema-less first import or new reviewed StatisticalVariables for these four ALW measures. After design approval, the curator can supply cleaned CSV/TMCF artifacts, preprocessing code, validation reports, and the required pull request.

Contact: Assaf Ichaki, assaf@californiacarecompass.com
