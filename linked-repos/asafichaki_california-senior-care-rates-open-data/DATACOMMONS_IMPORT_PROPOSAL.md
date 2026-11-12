# Data Commons import-design proposal (preparation only)

Status: LIVE PREPARATION ASSET 2026-07-22. Not yet submitted to Data Commons.
Google Data Commons routes dataset suggestions to a signed-in Google Issue
Tracker template (component 1660823). This document is the review-ready design;
submission is queued until an authenticated Google session is available. No Data
Commons approval, endorsement, import, or backlink is claimed.

## Dataset
California IHSS Individual Provider County Wage Rates 2026 (CC BY 4.0).
Canonical page: https://californiacarecompass.com/data/california-ihss-county-wages-2026
Repository: https://github.com/asafichaki/california-senior-care-rates-open-data

## What it measures
The county-set hourly wage paid to an IHSS Individual Provider (in-home
caregiver) under California's Medi-Cal In-Home Supportive Services program, as
approved by CDSS. This is a government program wage, NOT a private-pay price.

## Geographic mapping
All 58 counties map to verified Census-FIPS-based Data Commons `geoId` DCIDs;
California is `geoId/06`. The first proposed import comprises 58 county wage
observations for 2026.

## Schema question (not manufactured)
The current Data Commons schema does not contain an IHSS Individual Provider
wage StatisticalVariable. This proposal asks the Data Commons team whether to
use a schema-less first import or approve a new StatisticalVariable
(for example `Median_Wage_IHSSIndividualProvider`). It does not invent a final
DCID. Observation date: 2026; unit: USD per hour.

## Provenance
Every value is fetched live from the CDSS IHSS county wage workbook
(`ip-cc-wages-by-county.xlsx`, worksheet "IP Effective 10-1-2026") by
`scripts/fetch_ihss_county_wages.py`, retrieved 2026-11-11.
