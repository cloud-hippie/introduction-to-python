from flask import Flask, redirect, url_for, request
from tiny_api.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db) # this


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

@app.route('/',methods=["POST", "GET"])
def hello():
    if request.method == "GET":
        return User.query.all()
    return "Hello World!"

@app.route('/<name>', )
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()