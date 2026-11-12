# pipenv

**Source:** https://docs.pipenv.org

---

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. Windows is a first-class citizen, in our world.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever-important Pipfile.lock , which is used to produce deterministic builds.

Pipenv is primarily meant to provide users and developers of applications with an easy method to setup a working environment. For the distinction between libraries and applications and the usage of setup.py vs Pipfile to define dependencies, see ☤ Pipfile vs setup.py .

The problems that Pipenv seeks to solve are multi-faceted:

You no longer need to use pip and virtualenv separately. They work together.

Managing a requirements.txt file can be problematic, so Pipenv uses Pipfile and Pipfile.lock to separate abstract dependency declarations from the last tested combination.

Hashes are used everywhere, always. Security. Automatically expose security vulnerabilities.

Strongly encourage the use of the latest versions of dependencies to minimize security risks arising from outdated components.

Give you insight into your dependency graph (e.g. $ pipenv graph ).

Streamline development workflow by loading .env files.

If you’re on MacOS, you can install Pipenv easily with Homebrew:

Otherwise, refer to the ☤ Installing Pipenv chapter for instructions.

Pipenv & Virtual Environments ☤ Make sure you’ve got Python & pip ☤ Installing Pipenv ☤ Installing packages for your project ☤ Using installed packages ☤ Next steps

Release and Version History 2018.7.1 (2018-07-01) 2018.6.25 (2018-06-25)

Enables truly deterministic builds , while easily specifying only what you want .

Generates and checks file hashes for locked dependencies.

Automatically install required Pythons, if pyenv is available.

Automatically finds your project home, recursively, by looking for a Pipfile .

Automatically generates a Pipfile , if one doesn’t exist.

Automatically creates a virtualenv in a standard location.

Automatically adds/removes packages to a Pipfile when they are un/installed.

Automatically loads .env files, if they exist.

The main commands are install , uninstall , and lock , which generates a Pipfile.lock . These are intended to replace $ pip install usage, as well as manual virtualenv management (to activate a virtualenv, run $ pipenv shell ).

A virtualenv will automatically be created, when one doesn’t exist.

When no parameters are passed to install , all packages [packages] specified will be installed.

To initialize a Python 3 virtual environment, run $ pipenv --three .

To initialize a Python 2 virtual environment, run $ pipenv --two .

Otherwise, whatever virtualenv defaults to will be the default.

graph will show you a dependency graph of your installed dependencies.

shell will spawn a shell with the virtualenv activated.

run will run a given command from the virtualenv, with any arguments forwarded (e.g. $ pipenv run python or $ pipenv run pip freeze ).

check checks for security vulnerabilities and asserts that PEP 508 requirements are being met by the current environment.

Basic Usage of Pipenv ☤ Example Pipfile & Pipfile.lock ☤ General Recommendations & Version Control ☤ Example Pipenv Workflow ☤ Example Pipenv Upgrade Workflow ☤ Importing from requirements.txt ☤ Specifying Versions of a Package ☤ Specifying Versions of Python ☤ Editable Dependencies (e.g. -e . ) ☤ Environment Management with Pipenv ☤ About Shell Configuration ☤ A Note about VCS Dependencies ☤ Pipfile.lock Security Features

☤ General Recommendations & Version Control

Advanced Usage of Pipenv ☤ Caveats ☤ Specifying Package Indexes ☤ Using a PyPI Mirror ☤ Injecting credentials into Pipfiles via environment variables ☤ Specifying Basically Anything ☤ Deploying System Dependencies ☤ Pipenv and Other Python Distributions ☤ Generating a requirements.txt ☤ Detection of Security Vulnerabilities ☤ Community Integrations ☤ Open a Module in Your Editor ☤ Automatic Python Installation ☤ Automatic Loading of .env ☤ Custom Script Shortcuts ☤ Support for Environment Variables ☤ Configuration With Environment Variables ☤ Custom Virtual Environment Location ☤ Testing Projects ☤ Shell Completion ☤ Working with Platform-Provided Python Components ☤ Pipfile vs setup.py ☤ Changing Pipenv’s Cache Location ☤ Changing Default Python Versions

☤ Injecting credentials into Pipfiles via environment variables

☤ Configuration With Environment Variables

☤ Working with Platform-Provided Python Components

Specify which version of Python virtualenv should use.

Output diagnostic information for use in Github issues.

Clears caches (pipenv, pip, and pip-tools).

Checks for security vulnerabilities and against PEP 508 markers provided in Pipfile.

Specify which version of Python virtualenv should use.

Given a code path, show potentially unused dependencies.

Ignore specified vulnerability during safety checks.

Uninstalls all packages not specified in Pipfile.lock.

Specify which version of Python virtualenv should use.

Displays currently-installed dependency graph information.

Installs provided packages and adds them to Pipfile, or (if none is given), installs all packages.

Specify which version of Python virtualenv should use.

Ignore Pipfile when installing, using the Pipfile.lock.

Install dependencies one-at-a-time, instead of concurrently.

Ignore locking mechanisms when installing—use the Pipfile, instead.

Abort if the Pipfile.lock is out-of-date, or Python version is wrong.

Keep out-dated dependencies from being updated in Pipfile.lock.

Specify which version of Python virtualenv should use.

Generate output compatible with requirements.txt.

Generate output compatible with requirements.txt for the development dependencies.

Keep out-dated dependencies from being updated in Pipfile.lock.

Specify which version of Python virtualenv should use.

Spawns a command installed into the virtualenv.

Specify which version of Python virtualenv should use.

Specify which version of Python virtualenv should use.

Run in shell in fancy mode (for elegantly configured shells).

Always spawn a subshell, even if one is already spawned.

Installs all packages specified in Pipfile.lock.

Additionally install package(s) in [dev-packages].

Specify which version of Python virtualenv should use.

Install dependencies one-at-a-time, instead of concurrently.

Un-installs a provided package and removes it from Pipfile.

Specify which version of Python virtualenv should use.

Un-install all package from [dev-packages].

Purge all package(s) from virtualenv. Does not edit Pipfile.

Keep out-dated dependencies from being updated in Pipfile.lock.

Specify which version of Python virtualenv should use.

Keep out-dated dependencies from being updated in Pipfile.lock.

Install dependencies one-at-a-time, instead of concurrently.
