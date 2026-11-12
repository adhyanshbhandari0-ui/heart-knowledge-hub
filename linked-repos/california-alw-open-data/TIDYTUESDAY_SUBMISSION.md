- [x] This dataset has not already been used in TidyTuesday.
- [x] The dataset is less than 20MB when saved as tidy CSV files.
- [x] I can imagine visualizations of facility distribution, licensed capacity, geographic access, and the statewide waitlist-to-enrollment gap.

- [x] **title:** California Assisted Living Waiver Access
- [x] **article:**
  - [x] **title:** California ALW Waitlist and County Availability Tracker 2026
  - [x] **url:** https://californiacarecompass.com/data/california-alw-county-tracker-2026
- [x] **data_source:**
  - [x] **title:** California ALW Open Data repository
  - [x] **url:** https://github.com/asafichaki/california-alw-open-data
- [x] **images:**
  - [x] **file:** https://raw.githubusercontent.com/asafichaki/california-alw-open-data/main/examples/county-licensed-capacity.svg
  - [x] **alt:** Horizontal bar chart showing licensed Assisted Living Waiver participant-enrollment-unit capacity in each of the 15 participating California counties. Los Angeles has the largest capacity.

The proposed data includes a 1,224-row facility table and a 15-row county summary. The facility data is derived from the public California Department of Health Care Services ArcGIS layer. The county table also includes the statewide DHCS enrollment and waitlist totals. A key interpretation constraint is documented throughout: DHCS publishes one statewide waitlist, not county-level waitlists, and licensed capacity is not a live vacancy count.

- [x] **cleaning_script:**

```r
library(readr)
library(dplyr)

facilities_url <- paste0(
  "https://raw.githubusercontent.com/asafichaki/",
  "california-alw-open-data/main/california-alw-facilities-2026.csv"
)
counties_url <- paste0(
  "https://raw.githubusercontent.com/asafichaki/",
  "california-alw-open-data/main/california-alw-county-tracker-2026.csv"
)

alw_facilities <- read_csv(facilities_url, show_col_types = FALSE) |>
  mutate(
    zip_code = as.character(zip_code),
    source_access_date = as.Date(source_access_date)
  ) |>
  arrange(county, city, business_name, provider_number)

alw_counties <- read_csv(counties_url, show_col_types = FALSE) |>
  mutate(
    alw_available = alw_available == "yes",
    source_access_date = as.Date(source_access_date)
  ) |>
  arrange(desc(licensed_capacity_peu))
```

The repository also contains the standard-library Python script that fetches the source ArcGIS layer directly and documents why the GIS-derived `CountyName` field is used to resolve 11 conflicting free-text county values:
https://github.com/asafichaki/california-alw-open-data/blob/main/scripts/fetch_dhcs_alw_facilities.py

- [x] **data_dictionary:**

### `alw_facilities`

| variable | class | description |
|:--|:--|:--|
| provider_number | character | Provider number published in the DHCS layer. |
| legal_name | character | Facility legal name. |
| business_name | character | Facility business name. |
| capacity_per_peu | integer | Licensed participant-enrollment-unit capacity; not live vacancies. |
| address | character | Street address. |
| address_2 | character | Additional address line where published. |
| city | character | City. |
| county | character | GIS-derived California county. |
| zip_code | character | ZIP code. |
| phone_number | character | Public facility phone number from DHCS. |
| latitude | double | Latitude. |
| longitude | double | Longitude. |
| source_access_date | date | Date the DHCS source layer was accessed. |

### `alw_counties`

| variable | class | description |
|:--|:--|:--|
| county | character | California county with participating ALW facilities. |
| alw_available | logical | Whether participating ALW facilities are present. |
| participating_facilities | integer | Count of participating facilities. |
| licensed_capacity_peu | integer | Sum of licensed participant-enrollment-unit capacity. |
| statewide_enrolled | integer | Statewide ALW enrollment for the reporting month. Repeated to preserve context; not county enrollment. |
| statewide_waitlist | integer | Statewide ALW waitlist for the reporting month. Repeated to preserve context; not a county waitlist. |
| statewide_as_of | character | Reporting month for statewide totals. |
| source_access_date | date | Date the government sources were accessed. |

License: CC BY 4.0. The repository includes `CITATION.cff`, Frictionless Data metadata, direct CSV/JSON downloads, source references, and a reproducible visualization script.
