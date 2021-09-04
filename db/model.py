# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql.sqltypes import Boolean
from flask_login import UserMixin
from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import os, sys
sys.path.append(os.path.abspath(".."))

Base=declarative_base()

# bcrypt = Bcrypt(app)
sqliteFile="sample_sqlite3"
engine = create_engine(f'sqlite:///{sqliteFile}', echo=False)

session = scoped_session(sessionmaker(bind=engine))

class User(Base,UserMixin):
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

# テーブルを作成する．dev_test=True->初期データ挿入
def createTable(dev_test=False):
    engine.execute('PRAGMA foreign_keys = true;')
    Base.metadata.create_all(bind=engine)

    if dev_test:
        print('pass')
        try:
            univ = Univercity(univercityName="japan imperial Univ",
                                domainAddr="abc.ac.jp")
            session.add(univ)
            session.commit()
            user = User(name="carlos", birthday=20000421, univercityId=univ.id,
                            mailAddr="test@abc.ac.jp", password="0421")
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