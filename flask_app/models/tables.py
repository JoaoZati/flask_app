from flask_app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    @property
    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __init__(self, username, password, name, email):
        self.email = email
        self.name = name
        self.password = password
        self.username = username

    def __repr__(self):  # forma bonita de expor registros
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=id_user)

    def __init__(self, content, user_id):
        self.user_id = user_id
        self.content = content

    def __repr__(self):
        return '<Post %r>' % self.id


class Follow(db.Model):
    __tablename__ = 'follow'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_follower = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=id_user)
    follower = db.relationship('User', foreign_keys=id_follower)


db.create_all()
db.session.commit()
