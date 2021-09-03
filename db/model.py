from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "tekitou"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ["waste_reuse_system_secret_key"]

db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    birthday = db.Column(db.Integer(length=4), nullable=False)
    univercityName = db.Column(db.String(length=30), nullable=False)
    mailAddr = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    category = db.Column(db.String(length=30), nullable=False, unique=True)
    dangerous = db.Column(db.Boolean(), nullable=False, unique=True)
    needCredential = db.Column(db.String(length=30), nullable=False, unique=True)
    expire = db.Column(db.Integer(length=4), nullable=False)

