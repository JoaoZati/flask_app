from flask_app import app
from flask import render_template


@app.route('/index')
@app.route('/')
def index():
    return render_template('templates/index.html')
