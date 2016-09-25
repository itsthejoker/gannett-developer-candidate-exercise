# A Solution in CherryPy

This is a solution for the Developer Candidate Exercise written in Python 3.4 using CherryPy as the web framework handler with Mako as the templating engine.

## Installation: Virtualenv
I highly recommend using virtualenv to install everything, as that just makes it much simpler. It's not necessary, though; if you don't want to use it or already have it, go ahead and skip to "Installation: Part Deux". If you're not familiar with virtualenv and why it's great, check out [this great resource](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for more information.

If you don't have virtualenv installed, you can install it by running `pip install virtualenv` to your local python installation. If your local python installation (the one that comes up when you just run `python` in a terminal) is Python 2.x, you'll need to make sure you have a version of Python 3 installed, as the two are incompatible for this use case. You can verify by just running `python3` in your terminal; if you have it, a shell will start right up.

If you don't have any version of Python 3.x installed, you can get the installer [here](https://www.python.org/downloads/).

Once we're sure of whether Python 3 is installed / the default installation, create a virtual environment (virtualenv) by `cd`-ing to the directory above where the code is located and running `virtualenv {directoryname} --python=python3`. If Python 3.x is your default installation, you don't need the flag at the end. This will install a local, virtual copy of Python and all its binaries into the folder with all the code. `cd` into the target directory and run `source bin/activate` to start the virtual environment; `deactivate` turns it off. (NOTE: If you're using Windows, the commands are not the same. Please refer to [this link](http://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html) to find more information on the Windows commands.)

## Installation: Part Deux
Start the virtualenv (or don't, that's cool too). Install the requirements by running `pip install -r requirements.txt` - it will run down the list and automatically grab the right versions of everything you need, including any dependencies.

If you want to run the testing suite before starting the server, run `py.test -s test_app.py` in your terminal. There should be 8 tests.

If you want to just run the server and give it a look, run `python main.py` to start the server. Load up your web browser of choice and navigate to "http://localhost:8080/" to view the website.

Good luck and let me know if you have any questions / concerns / thoughts!
