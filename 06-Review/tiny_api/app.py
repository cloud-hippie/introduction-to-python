from flask import Flask, request
import json
from tiny_api.config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

db.create_all()
db.session.commit()

@app.get('/users/all', methods=["POST","GET","PUT"])
def getUsers():
    return json.dumps({
        "users": User.query.all()
    })
     

@app.post("/users/new")
def createUser():
    request_data = request.get_json()
    if request_data == None:
        return "Invalid request"
    db.session.add(User(name=request_data["name"]))
    user = User.query.filter_by(name=request_data["name"]).first()
    return json.dumps({
       "name": user.name,
       "id":user.id
    })

@app.get('/users/update')
def updateUser():
    """This should update the name of a user given the id in the payload"""
    return "Updated User"


@app.get('/users/update')
def deleteUser():
    """This should delete the user given the id in the payload"""
    return "Deleted User"


if __name__ == '__main__':
    app.run()