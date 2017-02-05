#!/usr/bin/env python
import flask
from flask import request, session, Flask

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'


@app.route('/counter', methods=['GET', 'POST'])
def counter():
    if request.method.lower() == 'post':
        if 'count' not in session:
            session['count'] = 0
        else:
            session['count'] += 1
        print session['count']
        return "incremented"
    elif request.method.lower() == 'get':
        if 'count' not in session:
            session['count'] = 0
        return "counter = {}".format(session['count'])


@app.route('/counter-clear')
def clear_session():
    session.clear()
    return flask.redirect(flask.url_for('/'))


if __name__ == '__main__':
    app.run(host='localhost', port=int("8080"))
