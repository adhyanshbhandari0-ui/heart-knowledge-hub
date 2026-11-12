# expanded parameter in MultiRecord.wrsamp

**Source:** https://github.com/MIT-LCP/wfdb-python/pull/555

---

As raised in #554 , wfdb.io.Multirecord.wrsamp does not provide the option to pass expanded=True . This should be provided so that multifrequency signals can be written within the Multirecord class. This PR updates the wrsamp call to allow for expanded to be passed.

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

This makes sense.  But I think we should probably also have more validity checking when writing out multisegment records.

_check_segment_cohesion looks like somebody started to do that, but that function isn't used?!

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Thanks @bemoody ! I agree with your comment about additional validation. I've opened issue #557 to capture that. We can use separate PRs to implement those validations.

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .

Successfully merging this pull request may close these issues.

There was an error while loading. Please reload this page .

There was an error while loading. Please reload this page .
