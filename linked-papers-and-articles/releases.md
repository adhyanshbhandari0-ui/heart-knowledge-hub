# releases

**Source:** https://github.com/MIT-LCP/wfdb-python/releases

---

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Read The Docs workflow - upgrade from deprecated Ubuntu version by @briangow in #537

Add fsspec to Read The Docs requirement by @briangow in #536

Correct docstring for plot.py by @johndgiese in #539

Split style checks into separate workflow by @tompollard in #542

Limit NPY_PROMOTION_STATE to i386 test job only by @briangow in #552

Allow expanded parameter in MultiRecord.wrsamp by @briangow in #555

Clarify expanded signal format in docstrings by @briangow in #556

Fix intermittent test failures on Windows CI due to Tcl/Tk initialization race condition by @briangow in #558

Fix ADC gain formula by @briangow in #551

Update MultiHeaderMixin header formatting to match HeaderMixin formatting by @briangow in #544

Bugfix: Update summary printing when writing EDF files. by @SamJelfs in #531

Fix style issues flagged by formatter by @tompollard in #562

Bump version to 4.3.1 and update release notes. by @tompollard in #563

@johndgiese made their first contribution in #539

@larsoner made their first contribution in #561

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Bump Sphinx to 7.0.0 by @tompollard in #530

Integrate fsspec to enable accessing WFDB files from cloud URIs by @briangow in #523

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Add support for Numpy 2.0 Fixes were added to address changes to type promotion that led to overflow errors (e.g. #493 ).

Fix UnboundLocalError in GQRS algorithm Fixes the GQRS algorithm to address an UnboundLocalError .

Support write directory in csv_to_wfdb write_dir can now be specified when calling csv_to_wfdb .

Use uv for for package management Moves package management from poetry to uv.

Fix misordered arguments in util.lines_to_file Fixes misordered arguments in util.lines_to_file .

Allow signals to be written with unique samples per frame Adds capability to write signal with unique samps_per_frame to wfdb.io.wrsamp .

Allow expanded physical signal in calc_adc_params Updates calc_adc_params to allow an expanded physical signal to be passed. Previously only a non-expanded signal was allowed.

Allow selection of channels when converting to EDF Fixes the wfdb-to_edf() function to support an optional channels argument.

Migrates Ricker wavelet from SciPy to WFDB after deprecation The Ricker wavelet ( scipy.signal.ricker ) was removed in SciPy v1.15, so the original implementation was migrated to the WFDB package.

Miscellaneous style and typing fixes Various fixes were made to code style and handling of data types.

@ajadczaksunriselabs made their first contribution in #459

@tecamenz made their first contribution in #465

@SnoopJ made their first contribution in #472

@dependabot made their first contribution in #477

@agent3gatech made their first contribution in #514

@SamJelfs made their first contribution in #519

@wenh06 made their first contribution in #526

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Handle more than 8 compressed signals in wrsamp by @bemoody in #450

Add a test to check if wrsamp can write more than 8 channels to format 516 by @alistairewj in #451

Use int64 instead of int for ann2rr by @bemoody in #454

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Removing upper bounds on dependencies ( #448 , #447 )

Miscellaneous style and typing fixes ( #445 , #440 )

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Converting a record into a Pandas DataFrame ( #380 )

Locating signals in a multi-segment record ( #403 )

Writing custom annotation symbols ( #404 )

Performance improvements when writing annotations ( #406 )

Correct rounding when converting floating-point signal data ( #419 )

Writing signals in compressed format ( #420 )

Decoding non-ASCII text in EDF files ( #429 )

Bug fixes when writing signal metadata ( #424 )

Documentation updates ( #401 , #407 , #433 , #437 )

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Supports reading WFDB records that contain FLAC signal files. #372

Switches to Poetry for package management. #356

Supports reading multi-frequency multi-segment records. #331

Supports plotting multi-frequency data using plot_wfdb . ​​ #348

Plots annotations on top of signals in plot functions. #345

Aligns signals horizontally in plot_wfdb if possible by default. #390

Correctly handles sample numbers > 2**31 in annotation files. #328

Fixes bugs when reading formats 8, 310, and 311. #327

Removes the ability for rdrecord and rdsamp to read EDF and WAV files. #370

Renames edf2mit , mit2edf , wav2mit , mit2wav , and csv2mit to read_edf , wfdb_to_edf , read_wav , wfdb_to_wav , and csv_to_wfdb respectively. #370 See also this note .

Moves the above format conversion functions to the wfdb.io.convert submodule. #370

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

This release makes the following changes:

Fix axes indexing issue when plotting a single channel: bugfix: unable to plot single channel record #308

Update matplotlib version and import only when used: This updates the Matplotlib version to avoid segmentation faults on Macs running Big Sur. #310 and Lazily import matplotlib #314

Performance improvements to smooth_frames=False: Optimize smooth_frames=False #318

List only direct dependencies in requirements.txt: Remove transitive dependencies #322

Correct an error in the calculation of the signals length for certain cases: Correctly infer length of record when unspecified #323

Speed up import time by removing the dependency on scikit-learn when it isn't required: Remove dependency on scikit-learn #321

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Adds conversion for CSV to WFDB-annotations

Adds information about WFDB header format in wfdb/io/_header.py

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Adds CSV to WFDB file converter (also TSV, and any other valid delimiter)

Updates documentation to include more functions

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .
