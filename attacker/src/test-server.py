from flask import Flask, request, send_file
import os
app = Flask(__name__)

@app.route('/get_picture', methods =['GET'])
def get_picture():
    body = request.get_json()
    user = body['user']
    print(body)
    try:
        path = os.path.join("../pictures", user + ".png")
        print(path)
        return send_file(path)
    except Exception as e:
        print(e)
        return e

if __name__ == '__main__':
    app.run(debug=True)
