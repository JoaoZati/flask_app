from flask_app import app


@app.route('/index')
@app.route('/')
def index():
    return '<center><p>Hello World</p></center>'


@app.route('/test')
@app.route('/test/<name>')
def test(name=None):
    if name:
        return f'<center><p>Olá {name}!</p></center>'

    return '<center><p>Olá usuario!</p></center>'
