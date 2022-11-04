# Tiny API

Tiny API is a minimal API to showcase how to use classes, dictionaries and methods.

## DB

The app is designed to communicate with a PostgreSQL database.

We reccomend using docker to run the database.

```bash
docker run --name tiny_api_db -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres
```

This will create a database called tiny_api_db and a user called postgres. It will run a Postgres server on port 5432.

You can go into the container and create the db in the container.

```bash
docker exec -it tiny_api_db bash
```

You are now in the container.

```bash
psql -U postgres
```

This logs you into the database.

Create a database called tiny_api.

```bash
CREATE DATABASE tiny_api;
```

Exit the postgres shell.

```bash
\q
```

Get out of the container.

```bash
exit
```

We cave now created a container that will also be our DB. It has postgres running on port 5432 and has it installed natively in the container.

## Application Logic

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
export DATABASE_URL=postgresql://postgres:mysecretpassword@localhost:5432/users
```

Then start the app.

```bash
$ flask run
```

The application is now running on port `5000`.

In another window, run the following command:

```bash
curl --location --request POST '127.0.0.1:5000/new' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"YOUR_NAME"
}'
```

This will create a new user in the database.

You will be able to see all the users, and the user you just created.




