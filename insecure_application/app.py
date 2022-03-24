from flask import Flask, request, jsonify, make_response, render_template, redirect, session
# from  werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime, timedelta
# from flask_sqlalchemy import SQLAlchemy
import logging
# import jwt
from flask_session import Session
from users.routes import blueprint as user_blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = '10101010101010'
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(user_blueprint)

# @app.route('/get_token', methods =['POST'])
# def verify():
#     body = request.get_json()
#     username = body['user_name']
#     password = body['password']
#     user1 = database.query.filter_by(user_name=username).first()

#     if user1 is not None:
#         if user1.password == password:
#             payload = {'exp': datetime.utcnow() + timedelta(minutes=30),'iat': datetime.utcnow(),'sub': user1.user_id}
#             print(type(payload), app.config['SECRET_KEY'])
#             token = jwt.encode(payload,app.config['SECRET_KEY'],algorithm='HS256')
#             return {"token": token}

#     return {"err":"Invalid User name or Password"}

if __name__ == '__main__':
    app.run(debug=True)
