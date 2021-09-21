from flask_app import app, login_manager
from flask import render_template
from flask_app.models.forms import LoginForm
from flask_app.models.tables import User


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)


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
    r = User.query.filter_by(username='Teste').first()
    print(r.username, r.name, r.id)
    return '<center><h1>Ok</h1></center>'
