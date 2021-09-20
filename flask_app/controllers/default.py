from flask_app import app


@app.route('/index')
@app.route('/')
def index():
    return '<center><p>Hello World</p></center>'


@app.route('/teste/<nome>')
def test(nome):
    return f'<center><p>Olá {nome}!</p></center>'
