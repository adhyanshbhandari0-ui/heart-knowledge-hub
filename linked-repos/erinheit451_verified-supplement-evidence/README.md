# Verified Supplement Evidence Database

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI](https://img.shields.io/badge/DOI-10.57967%2Fhf%2F9356-blue.svg)](https://doi.org/10.57967/hf/9356)

An open, evidence-graded dataset of dietary-supplement clinical data — dosing, form/bioavailability, drug–nutrient interactions, population need, and cost-per-effective-dose product comparisons. **Every clinical claim carries a PubMed PMID** so it can be verified against the primary source.

Compiled and maintained by [Verified Supplement Data](https://verifiedsupplementdata.com). This repository is the canonical open mirror; the same data is available on [Hugging Face](https://huggingface.co/datasets/erinheit451/verified-supplement-evidence) (DOI `10.57967/hf/9356`) and [Kaggle](https://www.kaggle.com/datasets/roses451/verified-supplement-evidence-database), and as a free live [JSON API](https://verifiedsupplementdata.com/api/v1/recommend/index.json).

## Tables

| File | Rows | What it holds |
|------|------|----------------|
| `data/supplement-evidence-v1.csv` | 72 | Flagship product table: dose, cost/day, third-party certification, evidence grade, PubMed IDs |
| `data/condition-ingredient-v1.csv` | 136 | Ingredient → condition relationships with evidence tier, dose, and PMIDs |
| `data/form-bioavailability-v1.csv` | 38 | Supplement forms (e.g. magnesium glycinate vs oxide) with absorption verdicts and clinical dose |
| `data/ingredient-master-v1.csv` | 26 | Per-ingredient rollup: clinical dose target, cost range, NHANES deficiency %, FAERS adverse-event signal |
| `data/medication-depletion-v1.csv` | 20 | Which medications deplete which nutrients (statins, metformin, PPIs, etc.), severity, mechanism, PMIDs |
| `data/population-need-v1.csv` | 15 | Population-specific deficiency prevalence and mechanisms |
| `data/top-pick-by-category.csv` | 26 | Editorial top pick per supplement category by cost-per-effective-dose |

All files are UTF-8 CSV with a header row.

## Methodology

Product data is normalized to **cost-per-clinically-effective-daily-dose** rather than cost-per-bottle, so products with different serving sizes and elemental content are comparable. Clinical claims are tied to PubMed identifiers (`pmids` / `pubmed_ids` columns). Certification reflects NSF / USP / IFOS third-party testing status. Deficiency prevalence is from NHANES; adverse-event signals are from FDA FAERS. Full method: https://verifiedsupplementdata.com/methodology/

## Citation

> Verified Supplement Data (2026). *Verified Supplement Evidence Database* (v1). CC BY 4.0. DOI: [10.57967/hf/9356](https://doi.org/10.57967/hf/9356). https://verifiedsupplementdata.com/data/

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) — free to use, share, and adapt with attribution.
