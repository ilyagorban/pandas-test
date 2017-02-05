#!/usr/bin/env python
import flask
from flask import request, Flask
import random

app = Flask(__name__, static_url_path="/resources", static_folder="resources")
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KM'


@app.route('/gify', methods=['GET'])
def gify():
    return flask.render_template('panda.html', pic="{}.jpg".format(random.choice(range(1, 8))))


if __name__ == '__main__':
    app.run(host='localhost', port=int("8080"))
