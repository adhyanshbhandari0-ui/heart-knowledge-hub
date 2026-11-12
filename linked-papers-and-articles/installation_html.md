# installation.html

**Source:** https://neuropsychology.github.io/NeuroKit/installation.html

---

Then, at the top of each of your Python script, you should be able to import the module:

Living on the edge? You can get the latest dev version from GitHub by running:

You are new to all this, and you’re not even sure if you have Python installed? Don’t worry, we’ll walk you through all of it.

You will need two things to program in Python, Python itself and an IDE software to edit and work with the Python scripts.

You can download Python from https://www.python.org/downloads/

You can download Python from https://www.python.org/downloads/

Once VS Code is launched, the next step is to add functionalities to support your development workflow. In particular, it is critical to get the Python Interactive extension

Once VS Code is launched, the next step is to add functionalities to support your development workflow. In particular, it is critical to get the Python Interactive extension

To start running some code, click New File and Ctrl+S to save the file into whichever directory in your computer you want, naming the file with a .py extension. Press Shift+Enter to send each line of code to an interactive window

To start running some code, click New File and Ctrl+S to save the file into whichever directory in your computer you want, naming the file with a .py extension. Press Shift+Enter to send each line of code to an interactive window

Another, perhaps easier option is to download a full distribution. The advantage of Winpython is its portability (i.e., works out of a folder) and default setup (convenient for science). However, it only exists for Windows .

Install it somewhere (the desktop is a good place). It creates a folder called WPyXX-xxxx

Install it somewhere (the desktop is a good place). It creates a folder called WPyXX-xxxx

In the WPyXX-xxxx folder, open WinPython Command Prompt.exe

In the WPyXX-xxxx folder, open WinPython Command Prompt.exe

Now you can proceed to running the PIP command mentioned at the top

Now you can proceed to running the PIP command mentioned at the top

The difference between the two is straightforward, miniconda is recommended if you don’t have much storage space and you know what you want to install. Similar to Winpython, Anaconda comes with a base environment, meaning you have basic packages pre-installed.
Here is some more information to help you choose between miniconda and Anaconda .

Download and install Miniconda or Anaconda (make sure the Anaconda3 directory is similar to this: C:\Users\<username>\anaconda3\ )

Download and install Miniconda or Anaconda (make sure the Anaconda3 directory is similar to this: C:\Users\<username>\anaconda3\ )

Open the Anaconda Prompt (search for it on your computer; see here for Mac users)

Open the Anaconda Prompt (search for it on your computer; see here for Mac users)

There should be a name in parentheses before your user’s directory, e.g. (base) C:\Users\<yourusername> . That is the name of your computing environment. By default, you have a base environment . We don’t want that, so create an environment.

Run conda env create <yourenvname> ; activate it every time you open conda by running conda activate <yourenvname>

Run conda env create <yourenvname> ; activate it every time you open conda by running conda activate <yourenvname>

If you have Python installed as part of Miniconda or Anaconda , please follow these steps:

As described in above, open the Anaconda Prompt and activate your conda environment

As described in above, open the Anaconda Prompt and activate your conda environment

You can now install NeuroKit2 from conda-forge by typing

You can now install NeuroKit2 from conda-forge by typing

conda or pip are the preferred methods to install NeuroKit2, as they will install the most up-to-date stable release.
