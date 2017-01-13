Exercise 1
----------

#Requirements

* python 2.7+ or 3.x
* pip (Python Package Index)
* virtualenvwrapper


## pip

Get `pip` by following the instructions
[here](http://stackoverflow.com/a/12476379)


## virtualenvwrapper

Once you have `pip` installed then install
[virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) which is a
set of extensions to Ian Bicking’s virtualenv tool. The extensions include
wrappers for creating and deleting virtual environments and otherwise managing
your development workflow, making it easier to work on more than one project at
a time without introducing conflicts in their dependencies.

```bash
jk@comp: $ pip install virtualenvwrapper==4.7.2
```

# Virtual environment

To create a new virtual environment simply issue:

```bash
jk@comp: $ mkvirtualenv ex1
```

Once the virtual environment was created successfully, you should see its name
at the beginning of the prompt line, e.g.:

```bash
(ex1) jk@comp: $
```

# Dependencies

This project has following dependencies:

* [behave](http://pythonhosted.org/behave/tutorial.html) - BDD Python style.
* [requests](https://pypi.python.org/pypi/requests) - Python HTTP for Humans.

Once you have `virtualenv` ready to go, we can then install the dependencies:

```bash
(ex1) jk@comp: $ pip install -r requirements.txt
```

# Running tests

To run all tests simply run `behave` command:

```bash
(ex1) jk@comp: $ behave
```
