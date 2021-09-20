from .wrapper import user_save
import unittest

from flask_sqlalchemy import SQLAlchemy, SignallingSession, orm

from . import create_app

class TestSignallingSession(SignallingSession):
    def commit(self):
        self.flush() # セッションが保持しているデータをすべてデータベースに書き込む
        self.expire_all() # セッションが保持してるデータをクリアしデータベースより読むこむようにする

class TestSQLAlchemy(SQLAlchemy):
    def create_session(self, options):
        return orm.sessionmaker(class_=SignallingSession, db=self, **options)

app=create_app()
db=TestSQLAlchemy(app)
session=db.session

class TestDB(unittest.TestCase):
  
  def test_register(self):
    user = user_save(user_name="carlos", univercity_name="kandai", email_address="k3897@k.ac.jp",password1="0421",birthday=20000421, univercityId=self.univ.id,db=db)
    #user_name univercity_name email_address password1 birthday univercity_id
    session.add(user)
    session.commit()
    bu = session.query(user_save).all()
    self.assertEqual(len(bu),1)
    self.assertEqual(bu[0] ,user)

if __name__ == '__main__':
    unittest.main()