# ENCLAI Reported Infectious-Disease Case Counts 2018–2024

**Source:** https://doi.org/10.5281/zenodo.21855170

---

Reported infectious-disease case counts under differing case definitions, 18 diseases, 2018–2024 — with the reporting-coverage denominator

(1) How much does case definition change the apparent size of an epidemic? Confirmed and suspected series are published paired, per country and year, from named originating authorities. In 2024 Brazil reports 6,579,385 laboratory-confirmed dengue cases and 10,330,277 suspected — a 57% difference for the same event.

(2) How much of an apparent multi-year trend in an aggregated surveillance collection is actually reporting coverage? Every annual row carries the number of countries reporting, so the two can be told apart.

WHY THE COVERAGE COLUMN MATTERS Countries reporting to this collection grew from 22 in 2018 to 99 in 2024. Seasonal influenza rises from 25,104 cases in 2018 to 917,338 in 2024 — a 37-fold increase that reads as an epidemic and is almost entirely one country joining in 2022. Dengue rises 25-fold over the same period while its reporting countries only double, and its largest reporter is present in every year: that rise is a real epidemic. Same table, opposite stories. Totals without a denominator invite the error.

CONTENTS alertx_open_panel_by_country_year.csv       1,622 rows: 18 diseases x 108 countries x 2018-2024, confirmed and suspected columns, originating authority named per row alertx_open_panel_annual_with_coverage.csv  annual totals WITH countries_reporting alertx_open_panel_withheld_cells.csv        44 cells excluded, each with its reason dataset_metadata.json                       method, limitations, SHA-256 checksums CHECKSUMS.sha256                            integrity

METHOD Counts aggregated with period-fit rules; running totals differenced rather than summed; national reporting supersedes subnational for the same population. Calendar-year windows with full prior history so cumulative counters anchor correctly. Confirmed and suspected are classified separately and are NEVER summed — the suspected series generally contains the confirmed one. Every cell passes a published quality gate before inclusion.

WITHHELD CELLS Cells failing a gate are withheld and listed with the reason rather than dropped silently. Gates: unnamed authority, thin support, single-period bulk, unclassified metric, implausible jump, and situation-report figure. The last exists because two national malaria figures (7,300,000 and 3,400,000) are single running-outbreak totals quoted in situation reports, not surveillance series. reports, not surveillance series.

LIMITATIONS * Reported surveillance counts, not modelled incidence or true burden. * Confirmed and suspected are two measurements of one population; adding them double-counts. * Coverage is uneven and changes over time. Do not read any annual series as a trend without the coverage columns. * Absence of a country means it did not report to this collection, not that the disease was absent. * Only complete calendar years are published, released once the following year has also closed.

SUPERSEDES version 1.0 (dengue only), 10.5281/zenodo.21855171.

METHOD SOFTWARE: https://doi.org/10.5281/zenodo.21855526

alertx_open_panel_annual_with_coverage.csv

Pan American Health Organization (PAHO/WHO) Arbovirus surveillance, PLISA. 2018-2024.

European Centre for Disease Prevention and Control (ECDC) Dengue surveillance. 2018-2024.

Brazil Ministry of Health — SINAN. Dengue notifications. 2018-2024.

This site uses cookies. Find out more on how we use cookies
