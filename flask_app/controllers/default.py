from flask_app import app, db
from flask import render_template
from flask_app.models.forms import LoginForm
from flask_app.models.tables import User


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


@app.route('/funcao/<info>')
@app.route('/funcao/', defaults={'info': None})
def funcao(info):
    r = User.query.filter_by(username='joaozati').all()
    print(r)
    return '<center><h1>Ok</h1></center>'
