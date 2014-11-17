# FileMakerLexer

FileMakerLexer is a plugin for the `pygments` python module.  It adds FileMaker calclation syntax highlighting to `pygments`.

## Installation

FileMakerLexer can be installed directly from github using `pip`:

```bash
$ sudo pip install git+https://github.com/johnchristopherjones/FileMakerLexer.git
```

For development, FileMakerLexer can be installed using setuptools:

```bash
$ git clone https://github.com/johnchristopherjones/FileMakerLexer.git
$ cd FileMakerLexer
$ sudo python setup.py developer
```

or using pip:

```bash
$ git clone https://github.com/johnchristopherjones/FileMakerLexer.git
$ sudo pip install --editable FileMakerLexer/filemakerlexer
```

Installing using setuptools allows you to link the cloned git repository into your python `dist-packages` directory so that any changes you make to the repo are instantly reflected in your python installation.
