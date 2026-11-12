# Sphinx

**Source:** https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html

---

Sphinx is a powerful documentation generator that
has many features for writing technical documentation.
Sphinx is written in Python, and supports documentation written in reStructuredText and Markdown.

Minimal configuration required to build an existing Sphinx project on Read the Docs looks like this,
specifying a Python 3.x toolchain on Ubuntu, using the built-in sphinx command,
and defining the location of the installation requirements:

If you have an existing Sphinx project you want to host on Read the Docs, check out our Adding a documentation project guide.

If you have an existing Sphinx project you want to host on Read the Docs, check out our Adding a documentation project guide.

If you’re new to Sphinx, check out the official Getting started with Sphinx guide.

If you’re new to Sphinx, check out the official Getting started with Sphinx guide.

For a step-by-step tutorial on Read the Docs using an example Sphinx project, take a look at the Read the Docs tutorial .

For a step-by-step tutorial on Read the Docs using an example Sphinx project, take a look at the Read the Docs tutorial .

Configuring Sphinx and Read the Docs Addons 

For optimal integration with Read the Docs, make the following optional configuration changes to your Sphinx config.

A canonical URL allows you to specify the preferred version of a web page
to prevent duplicated content.

Set your html_baseurl to your Read the Docs canonical URL using a Read the Docs environment variable :

If you’re using the Read the Docs Sphinx Theme , Server side search already works out of the box.

If you’re using a different theme, enable Server side search :

Add a snippet of JavaScript: readthedocs.js  // Trigger the Read the Docs Addons Search modal when clicking on "Search docs" input from the topnav. // NOTE: The selector of the search input may need to be adjusted based on your theme. document . querySelector ( "[role='search'] input" ). addEventListener ( "focusin" , () => { const event = new CustomEvent ( "readthedocs-search-show" ); document . dispatchEvent ( event ); });

Include it in your build: conf.py  html_js_files = [ ( "readthedocs.js" , { "defer" : "defer" }), ]

Integrate the Read the Docs version menu into your site navigation 

The Addons flyout menu displays differently depending on which Sphinx theme your documentation uses.

If you’re using the Read the Docs Sphinx Theme , the Addons flyout menu is already fully integrated into the theme. Use the theme options flyout_display , version_selector , language_selector to configure it.

If you’re using the Read the Docs Sphinx Theme , the Addons flyout menu is already fully integrated into the theme. Use the theme options flyout_display , version_selector , language_selector to configure it.

If you’re using another theme, the flyout menu displays in the bottom right of the docs.

If you’re using another theme, the flyout menu displays in the bottom right of the docs.

In either case, you can configure the flyout menu sorting and display options in Settings , under Addons .

You can use Markdown using MyST and reStructuredText in the same Sphinx project.
We support this natively on Read the Docs, and you can also use it locally by installing myst-parser :

You can now continue writing your docs in .md files and it will work with Sphinx.

Learn how to use MyST to write Markdown documentation in your Sphinx project.

Start writing Markdown in your existing reStructuredText project, or migrate it completely.

https://github.com/readthedocs/test-builds/tree/full-feature

https://test-builds.readthedocs.io/en/full-feature

An introduction to Sphinx and Read the Docs for technical writers

An introduction to Sphinx and Read the Docs for technical writers
