# RxTerms

**Source:** https://lhncbc.nlm.nih.gov/MOR/RxTerms

---

Official websites use .gov A .gov website belongs to an official government
              organization in the United States.

Secure .gov websites use HTTPS A lock ( Lock Locked padlock icon ) or https:// means youâve safely connected to
              the .gov website. Share sensitive information only on official,
              secure websites.

RxTerms is a drug interface terminology derived from RxNorm for prescription writing or medication history recording (e.g. in
        e-prescribing systems, PHRs).

Directly links to RxNorm, the U.S. drug terminology standard, and facilitates inclusion of RxNorm
            identifiers in electronic health records.

Efficient data entry - RxTerms separates the full names in RxNorm into two parts: drug name + route
            (e.g. INDERAL (Oral-pill)) and strength + dose form (e.g. 80 MG Tabs) to avoid big picklists with
            excessively long names. It excludes drugs from RxNorm that are obsolete or unavailable in the U.S.*

User-friendly features - commonly used synonyms and abbreviations (e.g. HCTZ for hydrochlorothiazide),
            "tall man" lettering recommended by FDA to avoid medication errors (e.g. ChlorproMAZINE and
            ChlorproPAMIDE).

Good coverage - retains the broad coverage of RxNorm for U.S. prescribable drugs - 99% coverage of both
            generic and brand names of U.S. most commonly prescribed drugs according to one assessment. RxTerms is
            tailored for U.S. prescribing and it might not be the right choice for many non-U.S. countries.

RxTerms is developed and maintained by the Lister Hill National Center for Biomedical
        Communications, NLM . Please directly email comments or questions to: NLM Support Center .

* Availability in U.S. is based on the Current Prescribable Content of RxNorm. This is an approximation and
        may not be 100% accurate.

RxTerms is published as a zip of files that may be loaded into a SQL database.  These files are described below.

Information from the current edition of RxTerms is also available via the RxTerms API .

The Clinical Table Search Service serves RxTerms among other data sets.

The RxTerms Demo offers auto-completion using the Clinical Table Search Service and LHC-Forms .

RxTerms is updated monthly following the RxNorm full monthly release, whose schedule can be found at the RxNorm Overview .

Sample load script for loading RxTerms into MySQL

An archive of older RxTerms releases is below.

These are the fields and their description:

RXCUI - the RxNorm unique identifier for the clinical drug, which can be one of the following term
            types: Semantic Clinical Drug (SCD) e.g. azithromycin 250 MG Oral Capsule. Semantic Branded Drug (SBD) e.g. azithromycin 250 MG Oral Capsule [Zithromax]. Generic Pack (GPCK) e.g. {6 (azithromycin 250 MG Oral Tablet) } Pack Branded Pack (BPCK) e.g. {6 (azithromycin 250 MG Oral Tablet [Zithromax]) } Pack [Z-PAKS].

Semantic Clinical Drug (SCD) e.g. azithromycin 250 MG Oral Capsule.

Semantic Branded Drug (SBD) e.g. azithromycin 250 MG Oral Capsule [Zithromax].

Generic Pack (GPCK) e.g. {6 (azithromycin 250 MG Oral Tablet) } Pack

Branded Pack (BPCK) e.g. {6 (azithromycin 250 MG Oral Tablet [Zithromax]) } Pack [Z-PAKS].

GENERIC_RXCUI - this is the corresponding generic clinical drug for SBD and BPCK (null for SCD).

FULL_NAME - the full RxNorm name of the clinical drug.

RXN_DOSE_FORM - dose form and intended route information from RxNorm.

FULL_GENERIC_NAME - the generic part of the full RxNorm name.

BRAND_NAME - the brand name part of the full RxNorm name (null for SCD). Brand names are in all
            uppercase to distinguish them from generic names.

DISPLAY_NAME - drug name (either generic or brand name) and intended route e.g. INDERAL (Oral-pill).

ROUTE - intended route derived from RXN_DOSE_FORM.

NEW_DOSE_FORM - dose form derived from RXN_DOSE_FORM.

STRENGTH - strength information parsed from the RxNorm full name.

SUPPRESS_FOR - to flag drug names deemed not likely to be useful for data entry. For example, long
            generic drug names with multiple ingredients (e.g. Bacitracin/Hydrocortisone/Neomycin/Polymyxin B) are
            suppressed because they are almost always prescribed by their brand names (e.g. CORTISPORIN OINTMENT).
            Any non-null value means that a row should be suppressed.

DISPLAY_NAME_SYNONYM - commonly used synonyms or abbreviations for the drug e.g. MOM for Milk of
            Magnesia.

IS_RETIRED - to flag records that existed in earlier versions but not in the latest version.

SXDG_RXCUI - the RxNorm unique identifier for the entity represented by the DISPLAY_NAME (drug +
            intended route). The corresponding TTY (term type) in RxNorm is either SCDG (Semantic Clinical Doseform
            Group) or SBDG (Semantic Branded Doseform Group), as represented in the field SXDG_TTY.

SXDG_TTY - the RxNorm TTY of the semantic doseform group

SXDG_NAME - the RxNorm name of the semantic doseform group

The fields DISPLAY_NAME, DISPLAY_NAME_SYNONYM, NEW_DOSE_FORM and STRENGTH are probably the most useful. We
        advise you to exclude rows that are suppressed or retired (i.e. rows with non-null values in SUPPRESS_FOR or
        IS_RETIRED).

Ingredients file - Ingredients(version).txt (available after 201106 release)

This file lists the ingredients and their RXCUIs for every drug in RxTerms that is not suppressible or
        retired.

RXCUI - the RxNorm uniquie identifier for the clinical drug
