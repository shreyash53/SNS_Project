from flask import Flask, request, send_file, render_template
import os
import markdown

app = Flask(__name__)

with open("./templates/readme.md", "r") as f:
    mdtext = f.read()

mdhtml = markdown.markdown(mdtext, extensions=['md_in_html'])

@app.route('/', methods =['GET'])
def get_picture():
    try:
        return mdhtml
    except Exception as e:
        print(e)
        return e

if __name__ == '__main__':
    app.run(debug=True)
