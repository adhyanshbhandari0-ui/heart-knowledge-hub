# Semantic Scholar Open Research Corpus

**Source:** https://allenai.org/data/s2orc

---

S2ORC: The Semantic Scholar Open Research Corpus

S2ORC is a general-purpose corpus for NLP and text mining research over scientific papers.

S2ORC was developed by Kyle Lo and Lucy Lu Wang at the Allen Institute for AI . It is now being maintained as a product offering by the API team at Semantic Scholar .

S2ORC is released under the ODC-By 1.0 .  By using S2ORC, you agree to the terms in the license.

Please cite our ACL 2020 paper if you use S2ORC for your project.  See the BibTeX . You can also watch our 12 min ACL 2020 talk .

It's Jan 2023; happy new year! After years of managing S2ORC as a research project, it has now been adopted as a core dataset offering through the Semantic Scholar Public API . Please look for the instructions under "Bulk Dataset" for download!

S2ORC is now available through the Semantic Scholar Public API as a "Bulk Dataset". It is continuously being rebuilt so if you access it through there, you'll get access to new papers as well!

Released s2orc-doc2json to support parsing of PDF and LaTeX to JSON format.

Released a new version of S2ORC containing papers up until 2020-04-14, bringing full text coverage from 8M to 12M.

Released a new version of S2ORC containing papers up until 2020-04-14, bringing full text coverage from 8M to 12M.

Lifted some paper filters to be more lenient toward papers that don't have sufficient amount of text.  This brought total paper count to 136M from 81M.

Lifted some paper filters to be more lenient toward papers that don't have sufficient amount of text.  This brought total paper count to 136M from 81M.

Updated the schema to keep paper metadata and parsed paper text separate.

Updated the schema to keep paper metadata and parsed paper text separate.

Fixed major bugs such as (i) missing section names, (ii) inline citation mention links that don't resolve to bibliographies, and (iii) unpredictable typing in certain metadata fields.

Fixed major bugs such as (i) missing section names, (ii) inline citation mention links that don't resolve to bibliographies, and (iii) unpredictable typing in certain metadata fields.

Omitted LaTeX parses from this release.  They will be added in a subsequent release.  Part of the dataset schema change is to accommodate incremental releases (e.g. LaTeX-only release without having to re-run PDF parsing).

Omitted LaTeX parses from this release.  They will be added in a subsequent release.  Part of the dataset schema change is to accommodate incremental releases (e.g. LaTeX-only release without having to re-run PDF parsing).

Feb 2023 update: We are no longer supporting access to this version & recommend everyone use the latest way of accessing S2ORC through the Semantic Scholar Public API.  If you must use this version and need assistance, please contact Kyle and Lucy.

Feb 2023 update: We are no longer supporting access to this version & recommend everyone use the latest way of accessing S2ORC through the Semantic Scholar Public API.  If you must use this version and need assistance, please contact Kyle and Lucy.

We've changed the name of the project to S2ORC.  We will update the preprint shortly with the new name.

The BibTeX citation has also been changed to reflect this.

Feb 2023 update: We are no longer supporting access to this version & recommend everyone use the latest way of accessing S2ORC through the Semantic Scholar Public API.  If you must use this version and need assistance, please contact Kyle and Lucy.

Statistics: 81M+ paper nodes; 73M+ gold abstracts; 8M+ full text papers

Due to release bugs (e.g. missing section names), we no longer recommend usage of this version.  If you must use this version and need assistance, please contact Kyle and Lucy.

The original S2ORC dataset files were refactored into multiple datasets available through the Semantic Scholar APIs (See detailed documentation here ).

Once you obtain an API key from Semantic Scholar Public API , you should be able to access these bulk dumps like so:

For questions, feature requests, bug reports, please search existing issues on the s2-folks Github repo before creating a new issue .

The best way to contact us is through email.  Don't hesitate to reach out about anything; we've helped a lot of people get started with the dataset, which can be a bit daunting given its size.

Email: Please include {kylel, lucyw, rodneyk on all correspondence.

Give us Feedback: Totally optional, but we'd love to hear how you're using this dataset & any feedback for improving it.  Send us an email or leave a Github Issue.

S2ORC is now being maintained by the S2 API product team. For questions, feature requests, bug reports, please search existing issues on the s2-folks Github repo before creating a new issue .

S2AG is everything that is covered in the literature graph, including Nodes (i.e. papers, authors) and Edges (i.e. citations, authorship). A paper in S2AG is represented by a bundle of Metadata, such as the Title, Authors, Year, Venue, Abstract, etc. You can download different releases of S2AG via the the Semantic Scholar APIs (See detailed documentation here ).

S2AG is everything that is covered in the literature graph, including Nodes (i.e. papers, authors) and Edges (i.e. citations, authorship). A paper in S2AG is represented by a bundle of Metadata, such as the Title, Authors, Year, Venue, Abstract, etc. You can download different releases of S2AG via the the Semantic Scholar APIs (See detailed documentation here ).

S2ORC is everything that is machine-readable full text of the paper, which we derive using models run on the paper's PDF. The original S2ORC dataset files are no longer available for download. They were refactored into multiple datasets available through the Semantic Scholar APIs (See detailed documentation here ).

S2ORC is everything that is machine-readable full text of the paper, which we derive using models run on the paper's PDF. The original S2ORC dataset files are no longer available for download. They were refactored into multiple datasets available through the Semantic Scholar APIs (See detailed documentation here ).

If you're unsure what to use or cite, please email us and we'd be happy to discuss your project with you.

Original S2ORC was a research project w/ original code. The current S2ORC is a reimplementation of the ideas from the research project within the Semantic Scholar data pipeline. As such, there can be differences due to low level implementation details being different.

Original S2ORC was a research project w/ original code. The current S2ORC is a reimplementation of the ideas from the research project within the Semantic Scholar data pipeline. As such, there can be differences due to low level implementation details being different.

Current S2ORC is maintained by a different team than the original researchers.

Current S2ORC is maintained by a different team than the original researchers.

Original S2ORC was released under a non-commercial license. The current S2ORC is released under an ODC-By 1.0 license. We ask that users take care to double-check whether their intended usage of S2ORC and its underlying contents is permissible under this license.

Original S2ORC was released under a non-commercial license. The current S2ORC is released under an ODC-By 1.0 license. We ask that users take care to double-check whether their intended usage of S2ORC and its underlying contents is permissible under this license.

S2ORC is currently released through the Semantic Scholar Public API under the ODC-By 1.0 . By using S2ORC, you are agreeing to its usage terms.

S2ORC: The Semantic Scholar Open Research Corpus: https://www.aclweb.org/anthology/2020.acl-main.447/
