from flask_app import app

@app.route('/index')
@app.route('/')
def index():
    return '<center><p>Hello World</p></center>'
