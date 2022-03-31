# Python Packages


## Create a virtual environment to install all your packages.

```bash
python3 -m venv module-demo
```

This creates a virtual environment in the current directory.

Use the virtual environment to install all the packages you need.

```bash
source module-demo/bin/activate
```

There are other platforms that allow us to create virtual environments and install packages. These are worth checking out.

[Poetry](https://poetry.eustace.io/)

[pipenv](https://pipenv.readthedocs.io/en/latest/)

## Install Python Packages through pip

```bash
pip install package_name
```

Keep a list of the dependencies you need to install.

```
touch requriments.txt
```

You can see all the currently installed packages by running:

```bash
pip list
```

Find the one you installed and its version and add it to the `requirements.txt` file.

Save the file and run the following command to install the packages:

```bash
pip install -r requirements.txt
```

