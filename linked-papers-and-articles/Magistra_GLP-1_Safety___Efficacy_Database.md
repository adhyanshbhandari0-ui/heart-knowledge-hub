# Magistra GLP-1 Safety & Efficacy Database

**Source:** https://magistra.health/en/data

---

An independent, transparent collection of GLP-1 and anti-obesity medication safety data, every point traceable to a citable source. The clinical, regulatory and news tracks update daily; the community track (Reddit, Drugs.com) has added no new report since 2026-05-28 — Reddit has blocked our collector since 2026-05-28.

Two drugs side by side: side-effect comparisons from trial results

Points in the 15 tracked effects. What we leave out

Where this corpus itself holds citable clinical rates, the card shows this corpus's pooled clinical figure (weighted rate with a confidence interval) with its basis right below it: how many stated rates from how many distinct sources — for some effects that is a single source, and the card says so. Where the corpus has no citable clinical rate for an effect yet, the card usually shows a fixed figure or range from the published literature, labelled "literature" — except for the one effect whose literature source itself states no rate: that card reads "No citable evidence" instead of a number (withdrawn 2026-09-03). Alongside it, the reporting frequency: the share of distinct community reports (reddit.com, drugs.com, one row per source URL) that mention the effect — not an incidence rate, not comparable to the clinical figure. Per-effect sources: the data API (rateBase.clinical, via /api/data?q=effect&id=<effect>).

Registry sampling bias, disclosed 10 September 2026 and corrected 16 September 2026: registry rows collected before 10 September through the rotation path were capped at the five highest-percentage arm rows per trial — a selection on the very figure we measure (19 of the 25 trials with stored registry rows at the time; the six pinned pivotal trials — SURMOUNT-1, SELECT, STEP 1, STEP 2, SURPASS-CVOT, retatrutide phase 2 — were never affected). The collector was fixed on 10 September and the 19 trials were re-collected in full between 10 and 16 September 2026 (every tracked non-placebo arm row the registry posts is stored, verified live against the registry on 16 September), so each study's entry in a pooled figure below is now the mean of every arm the registry posts for that term, not of its five highest. Per-trial measurements and the correction record (items 25 and 32): the published methodology.

Eat smaller meals, avoid fatty food, stay hydrated. Take the injection in the evening so you sleep through the worst.

Stay very hydrated. Avoid dairy and high-fibre foods initially. If it persists beyond 3 weeks, contact your doctor.

Increase water intake and add fibre-rich foods gradually. If it persists, or before you start any supplement, ask your pharmacist or doctor.

Make sure you still eat enough — ask your pharmacist or doctor what intake is right for you. Set reminders to eat if needed.

Stay hydrated. If headaches persist, or before you take anything for them, ask your pharmacist or doctor.

2 of 4 sources are SERIOUS adverse-event rates from a trial registry's SAE table, which understate all-cause incidence

If you experience severe stomach pain radiating to your back: STOP the medication immediately and go to the emergency room. Do not wait.

If fatigue persists or gets worse, discuss it with your pharmacist or doctor — they can check whether your eating pattern or something else needs attention.

Eat very small portions slowly. Avoid lying down after eating. If vomiting is persistent or severe, contact your doctor — dose reduction may help.

Eat smaller meals, avoid spicy and fatty foods. If pain is severe, persistent, or radiates to the back, see a doctor immediately to rule out pancreatitis.

Avoid eating shortly before bed. Sleep with your head slightly elevated. Avoid foods you find trigger it. Ask your pharmacist or doctor before taking anything for it.

3 of 14 sources are SERIOUS adverse-event rates from a trial registry's SAE table, which understate all-cause incidence

If you experience sudden sharp pain in the upper right abdomen, especially after eating, seek medical attention. Discuss the pace of your weight loss with your doctor.

If you notice hair shedding, ask your pharmacist or doctor before starting any supplement — they can advise what, if anything, is appropriate for you.

Rotate injection sites (thigh, abdomen, upper arm). Let the pen reach room temperature before injecting. Apply a cold compress if the area is irritated.

Drink enough fluids and stand up slowly. If you take blood pressure medication, ask your doctor whether it needs reviewing.

If you notice reduced enjoyment of activities you used to love, talk to your doctor. Maintaining social connections and physical exercise can help. This effect is still being studied.

Every source below has actually contributed data points — this list is derived from the corpus, not hand-maintained. The count is how many points that source has provided; "paused" means no new point in 30+ days.

Registry of clinical studies. Nearly every point here is an adverse-event count a trial posted with its results. Trials without posted results add no rates.

Health and medical journalism collected via Google News RSS, each article attributed to the outlet that ran it. The same search also returns X posts and Quora answers; those have no publisher behind them and are labelled by platform.

Posts from Reddit. The collector searches 26 GLP-1, weight-management and diabetes subreddits, but Reddit's search also returns posts from other communities (gallbladder, pregnancy and general-health forums), and most stored posts come from those. Only posts from the 26 configured communities count towards a published community figure; the rest are stored and screened out.

374 data points · latest 2026-05-28 paused

Abstracts of peer-reviewed papers (clinical trials, reviews, case reports and pharmacovigilance studies) from the world's largest biomedical literature database.

FDA Adverse Event Reporting System. Post-market safety surveillance data from the United States.

66 data points · latest 2026-08-13 paused

Structured patient experience data from Drugs.com medication reviews.

51 data points · latest 2026-08-12 paused

medRxiv preprints — findings released before peer review, labelled as such. The collector also searches bioRxiv, which has contributed no point yet. Withdrawn preprints are not counted.

Pages linked directly rather than found through PubMed or the news search: journal articles and, occasionally, newspaper reports.

Three layers: what the daily pipeline takes in and stores, which stored points do not count towards the total above, and which counted points carry no rate that goes into a pooled figure. Every number below is derived from the run reports and the database itself. The same figures are in the API under intakeAndExclusions (/api/data?q=overview).

Summed over 211 daily runs (7 Apr 2026 to 8 Nov 2026), and the latest run on its own. No run report is on record for 5 days in that period.

From item read to row extracted: an item drops out when the model finds no side effect in it (not relevant, or nothing extractable), when every row it yields falls outside the effect list or names a drug that is not GLP-1, or when the extraction call fails. How many items dropped for which reason: recorded in 35 of the 211 runs; earlier runs did not record it.

Breakdown by source (how many items and rows each source supplied and lost): see the table below for the latest run.

Reconciliation: the daily runs stored 4,187 rows in all. The database held 26 before the first run and 3,924 after the latest. The remaining net change, -289 rows, happened outside the daily collect step (for example one-off repairs, re-collections and removals) and is not itemised in the run reports.

The database holds 3,924 points. 3,551 of them count towards the data-point total on this page and in the API. The rest are kept but count nowhere:

150 seed rows from April 2026: written from our own static page, not collected from an external source. Kept as an audit trail.

223 rows in categories the extraction recognises but no page displays (temperature dysregulation 86, weight regain 69, muscle loss 51, kidney issues 16, menstrual irregularity 1).

A pooled clinical rate rests only on rows from clinical and regulatory sources that state a citable rate. Per effect: how many of those rows went into the rate, and why the rest did not. These are the same figures as rateBase.clinical.excluded on /api/data?q=effect&id=<effect>, so they include the seed rows from layer 2. Rows from community and news sources (896) feed the separate reporting frequency and are never pooled into a rate.

Access our data via a simple REST API. Free for academic use.

Get in touch for full dataset exports, custom queries, or collaboration opportunities.

Our data pipeline operates in five stages: (1) automated collection from 17 scrapers across four source categories, (2) LLM extraction using Claude Haiku for structured data from unstructured text, (3) two-track estimation that separately weighs clinical and community data, (4) random-effects confidence intervals for every corpus-derived estimate, and (5) log-odds patient modifiers that personalise risk based on sex, age, GI history, diabetes status, and dose tier.

Use the following citation when referencing our data in publications or research.

Magistra Health. "GLP-1 Safety Database: Comprehensive Side Effect Tracking from Clinical, Regulatory, and Real-World Sources." magistra.health/en/data. Accessed 12 November 2026 .

This database is continuously updated. Always include the access date in your citation.

A citable, dated snapshot of the corpus (full CSV plus a PDF brief) is available as a one-off purchase; bulk export and commercial use run via the subscription. See Data & API .

The Magistra-derived data layer — effect-level aggregations, rate estimates, reporting frequencies, and the methodology — is free to use for research and journalism with attribution (Magistra, magistra.health). Redistribution of the dataset itself is not permitted. Excerpts from third-party sources (PubMed abstracts, FAERS records, community posts) remain subject to their original publishers' terms. Bulk export and commercial use run via the research subscription.

The two static files (supply/demand forecast, India tracker) remain separately licensed CC BY 4.0, as stated on the data API page.

The per-effect pooled-rates summary table (rate, confidence interval, n, distinct sources) is separately licensed CC BY 4.0 and may be redistributed with attribution — download as CSV or JSON . The point-level corpus above is not covered by this.
