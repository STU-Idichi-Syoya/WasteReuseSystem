from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, sessionmaker
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import os, sys
sys.path.append(os.path.abspath(".."))
import run

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "tekitou"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ["waste_reuse_system_secret_key"]

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
engine = create_engine('sqlite:///sample_db.sqlite3', echo=True)
SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()

@login_manager.user_loader
def load_user(mailAddr):
    return session.query.get(mailAddr)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=30), nullable=False)
    birthday = db.Column(db.Integer(length=4), nullable=False)
    univercityId = relationship("Univercity")
    mailAddr = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)


class Univercity(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    univercityName = db.Column(db.String(), nullable=False)
    domainAddr = db.Column(db.String(length=30), nullable=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=30), nullable=False)
    category = db.Column(db.String(length=30), nullable=False, unique=True)
    dangerous = db.Column(db.Boolean(), nullable=False)
    needCredential = db.Column(db.String(length=30), nullable=False)
    expire = db.Column(db.Integer(), nullable=False)

