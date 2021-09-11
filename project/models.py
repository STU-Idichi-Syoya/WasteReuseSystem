# models.py

from flask_login import UserMixin
from . import db
from . import bcrypt


# ユーザ情報
class User(db.Model,UserMixin):
    __tablename__= 'users'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(length=30), nullable=False)
    birthday = db.Column(db.Integer(), nullable=False)
    univercity_id = db.Column(db.Integer(),db.ForeignKey("univercities.id"),nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

# 大学情報
class Univercity(db.Model,UserMixin):
    __tablename__= 'univercities'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    univercity_name = db.Column(db.String(), nullable=False)
    domain_addr = db.Column(db.String(length=30), nullable=True)

# 商品情報
class Item(db.Model,UserMixin):
    __tablename__= 'items'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id =  db.Column(db.Integer(),db.ForeignKey("users.id"),nullable=False)
    item_name = db.Column(db.String(length=30), nullable=False)
    category = db.Column(db.String(length=30), nullable=False, unique=True)
    dangerous = db.Column(db.Boolean(), nullable=False)
    need_credential = db.Column(db.String(length=30), nullable=False)
    expire = db.Column(db.Integer(), nullable=False)