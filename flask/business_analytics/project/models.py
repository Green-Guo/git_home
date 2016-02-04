from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r> % self.username'

class Program(db.Model):
    __tablename__ = 'programs'
    program = db.Column(db.String(100))

    def __init__(self, program):
        self.program = program

    def __repr__(self):
        return "<Program %r> % self.program"
