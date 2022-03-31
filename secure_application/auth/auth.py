from flask import Flask, request, jsonify, make_response, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.config['SECRET_KEY'] = '123459'
db = SQLAlchemy(app)
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class database(db.Model):
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(200))
    password = db.Column(db.String(200))

@app.route('/signup', methods = ['POST'])
def signup():
    body = request.get_json()
    username = body['user_name']
    password = body['password']
    print(username, password)
    record= database(user_name=username,password=password)
    try:
        db.session.add(record)
        db.session.commit()
        return {"message":"Added new user"}
    except:
        return {"message":"There was an issue adding the user"}

@app.route('/get_token', methods =['POST'])
def verify():
    body = request.get_json()
    username = body['user_name']
    password = body['password']
    user1 = database.query.filter_by(user_name=username).first()

    if user1 is not None:
        if user1.password == password:
            payload = {'exp': datetime.utcnow() + timedelta(minutes=30),'iat': datetime.utcnow(),'sub': user1.user_id}
            print(type(payload), app.config['SECRET_KEY'])
            token = jwt.encode(payload,app.config['SECRET_KEY'],algorithm='HS256')
            return {"token": token}

    return {"err":"Invalid User name or Password"}

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)