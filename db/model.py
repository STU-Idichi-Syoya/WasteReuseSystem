# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.sqltypes import Boolean

from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import os, sys
sys.path.append(os.path.abspath(".."))

Base=declarative_base()

# bcrypt = Bcrypt(app)
engine = create_engine('sqlite:///sample_sqlite3', echo=False)

SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()


class User(Base):
    __tablename__= 'users'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(length=30), nullable=False)
    birthday = Column(Integer(), nullable=False)
    univercityId = Column(Integer(),ForeignKey("univercities.id"),nullable=False)
    mailAddr = Column(String(length=50), nullable=False, unique=True)
    password = Column(String(length=60), nullable=False)


class Univercity(Base):
    __tablename__= 'univercities'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    univercityName = Column(String(), nullable=False)
    domainAddr = Column(String(length=30), nullable=True)

class Item(Base):
    __tablename__= 'items'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id =  Column(Integer(),ForeignKey("users.id"),nullable=False)
    name = Column(String(length=30), nullable=False)
    category = Column(String(length=30), nullable=False, unique=True)
    dangerous = Column(Boolean(), nullable=False)
    needCredential = Column(String(length=30), nullable=False)
    expire = Column(Integer(), nullable=False)

def createTable():
    engine.execute('PRAGMA foreign_keys = true;')
    Base.metadata.create_all(bind=engine,check_data=True)

def deleteTable():
    import os
    os.unlink("sample_sqlite3")
    
if __name__=='__main__':
    createTable()