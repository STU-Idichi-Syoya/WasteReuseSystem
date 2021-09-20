from .wrapper import user_save
import unittest

from flask_sqlalchemy import SQLAlchemy, SignallingSession, orm

from . import create_app
from project.wrapper import item_like, item_photo

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
        user0 = user_save(user_name="carlos", univercity_name="kandai", email_address="k3897@k.ac.jp", password1="0421", birthday=20000421, db=db)
        user1 = user_save(user_name="idichi", univercity_name="osaka", email_address="o3897@k.ac.jp",password1="1234",birthday=20000521,db=db)
        user2 = user_save(user_name="fukuda", univercity_name="sofia", email_address="s3897@k.ac.jp",password1="5678",birthday=20000621,db=db)
        user3 = user_save(user_name="michael", univercity_name="ritumei", email_address="r3897@k.ac.jp",password1="9012",birthday=20000721,db=db)
        user4 = user_save(user_name="tom", univercity_name="harvard", email_address="h3897@k.ac.jp",password1="3456",birthday=20000821,db=db)
        user5 = user_save(user_name="tony", univercity_name="mit", email_address="m3897@k.ac.jp", password1="7890", birthday=20000921, db=db)

        bu = session.query(user_save).all()
        self.assertEqual(len(bu), 1)

        self.assertEqual(bu[0] ,user1)
        self.assertEqual(bu[0], user2)
        self.assertEqual(bu[0] ,user3)
        self.assertEqual(bu[0] ,user4)
        self.assertEqual(bu[0] ,user5)

    def test_itemlike(self):
        like = item_like(is_like=True ,createrd_at="2021-09-20 21:04:15.412854" ,db=db)
        session.add(like)
        session.commit()
        bu = session.query(item_like).all()
        self.assertEqual(len(bu), 1)
        self.assertEqual(bu[0], like)
        
    def test_itemPhoto(self):
        photo = item_photo(photoNum=1 ,URI=1 ,db=db)
        session.add(photo)
        session.commit()
        bu = session.query(item_photo).all()
        self.assertEqual(len(bu), 1)
        self.assertEqual(bu[0] ,photo)

if __name__ == '__main__':
    unittest.main()