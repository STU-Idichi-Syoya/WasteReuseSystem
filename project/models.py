# models.py

from enum import unique
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
    is_active = db.Column(db.Boolean(), nullable=False,default=True)
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class UserSearchHistory(db.Model):
    __tablename__='user_search_histories'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    keyword = db.Column(db.String(length=60), nullable=False)

# 大学情報
class Univercity(db.Model):
    __tablename__= 'univercities'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    univercity_name = db.Column(db.String(), nullable=False)
    domain_addr = db.Column(db.String(length=30), nullable=True)

# 取引可能範囲
class PublicScope(db.Model):
    __tablename__= 'public_scopes'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    item_id =  db.Column(db.Integer(),db.ForeignKey("items.id"),nullable=False)
    permit_to_transaction_univ_id = db.Column(db.Integer(),db.ForeignKey("univercities.id"),nullable=False)
    
import datetime
# 商品情報
class Item(db.Model):
    __tablename__= 'items'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id =  db.Column(db.Integer(),db.ForeignKey("users.id"),nullable=False)
    item_name = db.Column(db.String(length=30), nullable=False)
    # 有効期限
    expire = db.Column(db.Time(), default=datetime.datetime.now().time())
    # お渡し場所
    place= db.Column(db.String(length=100), nullable=False)
    # 商品状態(正規化しない)
    state = db.Column(db.String(length=30), nullable=False)
    # 取引終了か？(貰い手決定)
    is_active=db.Column(db.Boolean(), nullable=False,default=True)
    # 出品者からのメッセージ
    message= db.Column(db.String(length=600), nullable=False)
    handing_method = db.Column(db.String(length=100), nullable=False)
    created_at= db.Column(db.Time(), default=datetime.datetime.now().time())

class ItemComment(db.Model):
    __tablename__= 'item_comments'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id =  db.Column(db.Integer(),db.ForeignKey("users.id"),nullable=False)
    item_id =  db.Column(db.Integer(),db.ForeignKey("items.id"),nullable=False) 
    comment=db.Column(db.String(length=600), nullable=False)
    # 自動付加
    created_at= db.Column(db.Time(), default=datetime.datetime.now().time())

class ItemBuy(db.Model):
    __tablename__= 'item_buys'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id =  db.Column(db.Integer(),db.ForeignKey("users.id"),nullable=False)
    item_id =  db.Column(db.Integer(),db.ForeignKey("items.id"),nullable=False) 
    created_at= db.Column(db.Time(), default=datetime.datetime.now().time())



class ItemLike(db.Model):
    __tablename__= 'item_likes'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id =  db.Column(db.Integer(),db.ForeignKey("users.id"),nullable=False)
    item_id =  db.Column(db.Integer(),db.ForeignKey("items.id"),nullable=False)
    is_like = db.Column(db.Boolean(), nullable=False,default=True)
    created_at= db.Column(db.Time(), default=datetime.datetime.now().time())
    

class ItemTag(db.Model):
    __tablename__= 'item_tags'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    item_id =  db.Column(db.Integer(),db.ForeignKey("items.id"),nullable=False) 
    tag_id = db.Column(db.Integer(),db.ForeignKey("tags.id"),nullable=False) 
    created_at= db.Column(db.Time(), default=datetime.datetime.now().time())

class Tag(db.Model):
    __tablename__= 'tags'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String(length=30), nullable=False,unique=True)
    created_at= db.Column(db.Time(), default=datetime.datetime.now().time())


class ItemPhoto(db.Model):
    __tablename__= 'item_photos'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    item_id =  db.Column(db.Integer(),db.ForeignKey("items.id"),nullable=False)
    # 各ItemのPhotoの順番を保証する（サムネイル用）
    photoNum= db.Column(db.Integer(),nullable=False)
    ## blobの場合、URI形式は/items/blob/:id
    URI = db.Column(db.String(),nullable=True)

## 直接保存
class ItemBlob(db.Model):
    __tablename__= 'item_photo_blob'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    item_id =  db.Column(db.Integer(),db.ForeignKey("item_photos.id"),nullable=False)
    ## 必ず小さい容量にすること
    blob = db.Column(db.LargeBinary(),nullable=False)