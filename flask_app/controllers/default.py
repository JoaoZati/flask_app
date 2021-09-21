from flask_app import app
from flask import render_template
from flask_app.models.forms import LoginForm


@app.route('/index/<user>')
@app.route('/', defaults={'user': None})
def index(user):
    return render_template('index.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Success')
    return render_template('login.html',
                           form=form)
