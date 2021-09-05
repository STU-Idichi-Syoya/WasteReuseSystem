# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql.sqltypes import Boolean
from waste import login_manager
from waste import bcrypt
from flask_login import UserMixin
from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import os, sys
sys.path.append(os.path.abspath(".."))

Base=declarative_base()
sqliteFile="sample_sqlite3"
engine = create_engine(f'sqlite:///{sqliteFile}', echo=False)
session = scoped_session(sessionmaker(bind=engine))

# ユーザ情報
class User(Base,UserMixin):
    __tablename__= 'users'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_name = Column(String(length=30), nullable=False)
    birthday = Column(Integer(), nullable=False)
    univercity_id = Column(Integer(),ForeignKey("univercities.id"),nullable=False)
    email_address = Column(String(length=50), nullable=False, unique=True)
    password_hash = Column(String(length=60), nullable=False)
    
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
class Univercity(Base):
    __tablename__= 'univercities'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    univercity_name = Column(String(), nullable=False)
    domain_addr = Column(String(length=30), nullable=True)

# 商品情報
class Item(Base):
    __tablename__= 'items'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id =  Column(Integer(),ForeignKey("users.id"),nullable=False)
    item_name = Column(String(length=30), nullable=False)
    category = Column(String(length=30), nullable=False, unique=True)
    dangerous = Column(Boolean(), nullable=False)
    need_credential = Column(String(length=30), nullable=False)
    expire = Column(Integer(), nullable=False)

# テーブルを作成する．dev_test=True->初期データ挿入
def createTable(dev_test=False):
    engine.execute('PRAGMA foreign_keys = true;')
    Base.metadata.create_all(bind=engine)

    if dev_test:
        print('pass')
        try:
            univ = Univercity(univercity_name="japan imperial Univ",
                                domain_address="abc.ac.jp")
            session.add(univ)
            session.commit()
            user = User(user_name="carlos", birthday=20000421, univercity_id=univ.id,
                        email_address="test@abc.ac.jp", password="0421")
            session.add(user)
            session.commit()
        except:
            pass
def deleteTable():
    import os
    session.close()
    engine.dispose()
    os.unlink("sample_sqlite3")

createTable(True)

if __name__=='__main__':
    createTable()
