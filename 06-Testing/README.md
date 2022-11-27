# Python Testing

This is a repo for source code to be able to learn Python testing.

## Installation

As this is a Python project, you will need to have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

Create a virtual environment for the project. This will allow you to install the dependencies for the project without affecting your global Python installation.

```bash
python3 -m venv venv
```

Activate the virtual environment.

```bash
source venv/bin/activate
```


## Usage

Each of the Subdirectories in this repo will have a README.md file that will explain how to use the code in that directory.

To run the tests, you will need to install the dependencies. You can do this by running the following command:

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

You can then run the tests by running the following command:

```bash
pytest
```