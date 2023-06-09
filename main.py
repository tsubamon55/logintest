import logging
from flask import Flask, jsonify, request, render_template, redirect, session
from datetime import timedelta

import server
import settings

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
app.secret_key = settings.select_key
app.permanent_session_lifetime = timedelta(minutes=settings.session_lifetime)


@app.route('/')
def hello():
    app.logger.info(session)
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect('/login')


@app.route('/api/logout', methods=["POST"])
def logout():
    app.logger.info(session)
    session.pop('username', None)
    return redirect('/login')


@app.route('/show')
def show():
    resp = server.show()
    return resp


@app.route('/account/register', methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    if server.register(username, password):
        return jsonify({'action': 'register', 'status': 'success'}), 200
    return jsonify({'action': 'register', 'status': 'fail'}), 200


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if server.login_verification(username, password):
            session['username'] = username
            return redirect('/')
        return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
