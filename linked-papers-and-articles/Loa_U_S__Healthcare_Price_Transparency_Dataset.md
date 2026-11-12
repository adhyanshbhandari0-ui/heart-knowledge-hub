# Loa U.S. Healthcare Price Transparency Dataset

**Source:** https://www.loacare.com/methodology

---

Medical Pricing Database and Hospital MRF Methodology

Loa's medical pricing database organizes hospital machine-readable file pricing, including gross charges, cash prices, and payer-negotiated rates, alongside CMS provider records and reviewed submissions. Learn how each source is collected, normalized, and limited.

By Ali Anari , Engineering at Loa · Updated Jul 29, 2026

See the data in use: Hospital price spread report .

Our primary data source is the Machine Readable Files (MRFs) that US hospitals are required to publish under the Hospital Price Transparency Rule (45 CFR 180) . This federal regulation, effective since January 2021, requires every hospital operating in the United States to make their standard charges publicly available in a machine-readable format.

These files contain gross charges, discounted cash prices, and payer-specific negotiated rates for every service a hospital provides, from a routine blood test to complex surgery.

In addition to MRF data, Loa can review provider-submitted price and profile updates before publication. Reviewed updates serve two purposes:

Gap filling - not all facilities have complete or up-to-date MRF files; reviewed provider updates can add source-labeled context

Price verification - comparing submitted prices against published MRF data helps reviewers catch outdated or conflicting listings

As of July 27, 2026, Loa's public directory includes 4,702 hospital profiles with current price data across all 50 states, representing 116,655 current hospital price rows . Coverage changes as hospitals publish or update their price transparency files.

Provider directory information for doctors and specialists comes from the CMS National Plan and Provider Enumeration System (NPI Registry), the official federal database of healthcare providers.

For each procedure and location, Loa selects one preferred current price per hospital, prioritizing reviewed and cash-price records when available. We then calculate summary statistics from up to 100 eligible source-labeled hospital rows in the geographic region:

Minimum listed price - the lowest selected source-labeled row in the area

Maximum price — the highest selected published rate

Median price — the middle value, less affected by outliers

Average price — the arithmetic mean of all rates

Procedures are identified by CPT (Current Procedural Terminology) codes, the standard billing codes used across the US healthcare system. Prices are standardized to allow fair comparison across facilities.

Hospitals are required to update their price transparency files at least annually. Loa continuously monitors and processes new files as hospitals publish them. The data shown on our healthcare pricing pages reflects the most recently available information from each hospital.

While we strive for accuracy and comprehensiveness, there are important limitations to be aware of:

Prices are estimates based on published data, not guaranteed quotes

Your actual cost depends on your insurance plan, deductible status, and clinical specifics

Not all hospitals have fully compliant price transparency files

Professional fees (e.g., radiologist interpretation) may be billed separately

Prices may change between when data was published and when you receive care

Loa provides a Model Context Protocol (MCP) server that allows AI assistants to access our pricing data programmatically. This enables tools like Claude to search CPT codes, compare source-labeled hospital prices, and retrieve current Loa estimates for users.

Product teams can use Loa's medical cost and health pricing API to retrieve the same source-labeled, non-PHI pricing information shown on our website.

Pricing data comes from hospital Machine Readable Files (MRFs) that US hospitals are required to publish under the Hospital Price Transparency Rule (45 CFR 180), plus Loa-reviewed provider submissions when available. Each public price should carry source context so users can confirm the current quote before care.

As of July 27, 2026, Loa's public directory includes 4,702 hospital profiles with current price data, representing 116,655 current hospital price rows. Coverage changes as hospitals publish or update their price transparency files.

Hospital MRF files are typically updated annually or more frequently. Loa processes new files as they become available. The pricing data on any given page reflects the most recent data from hospitals in that region.

Prices shown include gross charges, cash/self-pay rates, and in some cases payer-specific negotiated rates. The "cash price" reflects what a hospital charges patients who pay out-of-pocket without insurance. Loa selects one preferred current price per hospital, then calculates the displayed min, max, median, and average from up to 100 eligible source-labeled hospital rows for the procedure and area.

Prices shown are based on published hospital data and should be used as estimates for comparison purposes. Your actual cost may vary based on your specific clinical situation, insurance plan, facility fees, and other factors. Always confirm pricing directly with your provider before scheduling a procedure.

Provider information (doctors, specialists) comes from the CMS National Plan and Provider Enumeration System, commonly known as the NPI Registry. This is the official federal database of healthcare providers.

Hospital pricing data: Hospital Price Transparency Rule, 45 CFR Part 180, Centers for Medicare & Medicaid Services (CMS).

Provider data: National Plan and Provider Enumeration System (NPPES), Centers for Medicare & Medicaid Services (CMS).

Researchers, journalists, and product teams can cite this methodology page as the canonical description of the Loa U.S. Healthcare Price Transparency Dataset.

Use source-labeled data to compare options before confirming the current quote with your provider.
