from flask_app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Colum(db.String, unique=True)
    password = db.Colum(db.String)
    name = db.Colum(db.String)
    email = db.Colum(db.String, unique=True)

    def __init__(self, username, password, name, email):
        self.email = email
        self.name = name
        self.password = password
        self.username = username

    def __repr__(self):  # forma bonita de expor registros
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Colum(db.Integer, primery_key=True)
    content = db.Colum(db.Text)
    id_user = db.Colum(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_key=id_user)

    def __init__(self, content, user_id):
        self.user_id = user_id
        self.content = content

    def __repr__(self):
        return '<Post %r>' % self.id


class Follow(db.Model):
    __tablename__ = 'follow'

    id = db.Colum(db.Integer, primary_key=True)
    id_user = db.Colum(db.Integer, db.ForeignKey('users.id'))
    id_follower = db.Colum(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_key=id_user)
    follower = db.relationship('User', foreign_key=id_follower)
