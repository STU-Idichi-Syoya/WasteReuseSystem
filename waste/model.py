# from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from waste import bcrypt
from flask_login import UserMixin
import os, sys
from waste import app

sys.path.append(os.path.abspath(".."))

sqliteFile="sample_sqlite3"

app.config["SQLALCHEMY_DATABASE_URI"]=f'sqlite:///{sqliteFile}'
db=SQLAlchemy(app=app)
session=db.session

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
class Univercity(db.Model):
    __tablename__= 'univercities'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    univercity_name = db.Column(db.String(), nullable=False)
    domain_addr = db.Column(db.String(length=30), nullable=True)

# 商品情報
class Item(db.Model):
    __tablename__= 'items'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id =  db.Column(db.Integer(),db.ForeignKey("users.id"),nullable=False)
    item_name = db.Column(db.String(length=30), nullable=False)
    category = db.Column(db.String(length=30), nullable=False, unique=True)
    dangerous = db.Column(db.Boolean(), nullable=False)
    need_credential = db.Column(db.String(length=30), nullable=False)
    expire = db.Column(db.Integer(), nullable=False)

# 商品公開先リスト
class ItemAllow(db.Model):
    __tablename__= 'items_allows'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    item_id =  db.Column(db.Integer(),db.ForeignKey("items.id"),nullable=False)
    allow_univercity_id = db.Column(db.Integer(),db.ForeignKey("univercities.id"),nullable=False)

# テーブルを作成する．dev_test=True->初期データ挿入
def createTable(dev_test=False):
    if os.path.exists(sqliteFile):return
    db.create_all()
    print('creating...')
    try:
        univ = Univercity(univercity_name="japan imperial Univ",
                            domain_addr="abc.ac.jp")
        session.add(univ)
        session.commit()
        user = User(user_name="carlos", birthday=20000421, univercity_id=univ.id,
                    email_address="test@abc.ac.jp", password="0421")
        session.add(user)
        session.commit()
        item=Item(user_id=user.id,item_name='testItem',category='実験',dangerous=False,need_credential="",expire=100000)
        itemAllow=ItemAllow(item_id=item.id,allow_univercity_id=univ.id)
        session.add(item)
        session.add(itemAllow)

        session.commit()
    except:
        # import traceback
        # traceback.print_exc()
        print('already inserted')
def deleteTable():
    # import os
    # session.close()
    # engine.dispose()
    # os.unlink("sample_sqlite3")
    pass

if __name__=='__main__':
    print('model create')
    createTable()
