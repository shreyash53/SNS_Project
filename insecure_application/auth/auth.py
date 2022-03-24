from flask import Flask, request, jsonify, make_response, render_template, redirect
# import jwt


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.config['SECRET_KEY'] = '123459'
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


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
    app.run(debug=True)