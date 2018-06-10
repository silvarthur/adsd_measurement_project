from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Record(db.Model):
    __tablename__ = "user_record"

    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True)
    email = db.Column('email', db.String(30), unique=True)
    password = db.Column('password', db.Integer, unique=True)

    def __repr__(self):
        return 'The username of this user is: %r' % self.username