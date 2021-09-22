from flask_app import app, login_manager
from flask import render_template, flash, redirect, url_for
from flask_app.models.forms import LoginForm
from flask_app.models.tables import User
from flask_login import login_user, logout_user, login_required, current_user


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/usuario/<user>')
@app.route('/usuario', defaults={'user': None})
def usuario(user):
    if not current_user.is_authenticated:
        flash('Faça o login')
        return redirect(url_for('index'))
    if current_user.name == user:
        return render_template('usuario.html', user=user)
    return redirect(f"/usuario/{current_user.name}")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            name = user.name
            login_user(user)
            flash('Logged in')
            return redirect(f"/usuario/{name}")
        else:
            flash('Invalid loggin')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out')
    return redirect('/')
