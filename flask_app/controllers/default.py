from flask_app import app
from flask import render_template


@app.route('/index/<user>')
@app.route('/', defaults={'user': None})
def index(user):
    return render_template('index.html', user=user)


@app.route('/login')
def login():
    return render_template('login.html')
