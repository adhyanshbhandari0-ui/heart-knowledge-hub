# pip

**Source:** https://pip.pypa.io/en/stable

---

Topic Guides Authentication Caching Configuration Dependency Resolution More on Dependency Resolution HTTPS Certificates Local project installs Repeatable Installs Secure installs VCS Support Managing a different Python interpreter Pip is not a workflow management tool

Reference Build System Interface Requirement Specifiers Requirements File Format Installation Report pip inspect JSON output specification

Commands pip pip install pip uninstall pip inspect pip list pip show pip freeze pip check pip lock pip download pip wheel pip hash pip search pip index pip cache pip config pip debug

Development Getting Started Contributing Continuous Integration Issue Triage Architecture of pip’s internals Broad functionality overview Repository anatomy & directory structure Configuration File Handling Finding and choosing files ( index and PackageFinder ) Command Line Interface Options that control the installation process Release process Vendoring Policy

Architecture of pip’s internals Broad functionality overview Repository anatomy & directory structure Configuration File Handling Finding and choosing files ( index and PackageFinder ) Command Line Interface Options that control the installation process

Finding and choosing files ( index and PackageFinder )

Options that control the installation process

UX Research & Design How to Contribute UX Guidance UX Research Results About pip’s Users How Users Understand pip How pip users think about security How pip is used in interactive environments (i.e. CI, CD) pip Personas Prioritizing pip Features Providing an override to install packages with conflicting dependencies pip --force-reinstall pip search pip Upgrade Conflict Improving pip’s Documentation

UX Research Results About pip’s Users How Users Understand pip How pip users think about security How pip is used in interactive environments (i.e. CI, CD) pip Personas Prioritizing pip Features Providing an override to install packages with conflicting dependencies pip --force-reinstall pip search pip Upgrade Conflict Improving pip’s Documentation

How pip is used in interactive environments (i.e. CI, CD)

Providing an override to install packages with conflicting dependencies

Pip is the package installer for Python . You can use it to
install packages from the Python Package Index and other indexes.

If you want to learn about how to use pip, check out the following resources:

If you find bugs, need help, or want to talk to the developers, use our mailing
lists or chat rooms:

If you find any security issues, please report to security @ python . org

Pip does not collect any telemetry, however, it will send
non-identifying environment information (Python version, OS, etc.) to any remote indices
used, who may choose to retain such information. Please consult PyPI’s privacy
policy for their data collection and retention practices.
