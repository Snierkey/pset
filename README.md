# Pset

A Python package development tool that simplifies the process of creating, building, and publishing Python packages.

## Installation
Just clone this and run `pip install .` (inside virtual environment) because it's not published to PyPI


## Quick Start
Create a new Python package:

```bash
pset create mypackage --author "Your Name" --email "you@me.com"
```

Build your package:

```
cd mypackage
pset build
```

Publish to PyPI:

```bash
pset publish
```

## Features
* Create new Python packages with proper structure
* Generate setup.py and pyproject.toml files
* Initialize git repositories
* Create virtual environments
* Build packages for distribution
* Publish to PyPI and other repositories
* Manage dependencies

## Commands

### create
Create a new Python package with all necessary files and directories

### build
Build the package for distribution

### publish
Publish the package to PyPI or other repositories

### init
Initialize an existing directory as a Python package

### install
Install dependencies and add them to requirements files

## License

MIT License - see LICENSE file for details.
