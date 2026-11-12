# formula for ADC gain

**Source:** https://github.com/MIT-LCP/wfdb-python/pull/551

---

As pointed out by @tcpan in #515 there was a mistake in one of the formula's for calculating ADC gain. The calculation needs to compute the digital range first before mapping the physical range.

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

@tompollard , I've added tests of the gain calculation for when the baseline exceeds the boundary. For each boundary ( MAX_I32 and MIN_I32 ) the test:

creates a signal which will trigger the boundary overflow

checks that we enter the logic for adjusting the gain and baseline

verifies that a round-trip test of writing and reading produces the expected result within some tolerance

makes sure the ADC gain formula produces the expected result

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Successfully merging this pull request may close these issues.

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .
