# Tiny API

Tiny API is a minimal API to showcase how to use classes, dictionaries and methods.

It relies on Python 3.8

It is recommended you use `pyenv`

Within this repo, run the following command:

```bash
$ pyenv virtualenv --copies 3.8.3 tiny-api
```
This will create a virtual environment for you to use.

Install the following dependencies:

```bash
$ pip install -r requirements.txt
```

It is a flask app, to get Flask to work, you need to set an environment variable.

```bash
FLASK_APP=app.py
```

Then start the app.

```bash
$ flask run
```


