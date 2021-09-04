from .model import session
from .model import Univercity, User, createTable, deleteTable
import unittest

class ModelTestCase(unittest.TestCase):
    
    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        createTable()
        self.univ = Univercity(univercityName="japan imperial Univ",domainAddr="imperial.ac.jp")
        session.add(self.univ)
        session.commit()

    def tearDown(self):
        deleteTable()

    def testInsertUser(self):
        # Test feature one.
        user = User(name="carlos", birthday=20000421, univercityId=self.univ.id,
                    mailAddr="k3897@k.ac.jp", password="0421")
        session.add(user)
        session.commit()
        bu = session.query(User).all()
        self.assertEqual(len(bu),1)
        self.assertEqual(bu[0] ,user)

    def testNotFoundUser(self):
        usr=session.query(User).filter(User.id==1).first()
        self.assertEqual(None,usr)

    def testInsertDuplicateUser(self):
        usr=User(name='testName',birthday=1234,mailAddr='testaddr@axc.jp',password='str',univercityId=self.univ.id)
        session.add(usr)
        session.commit()
        try:
            usr=User(name='testName',birthday=1234,mailAddr='testaddr@axc.jp',password='str',univercityId=self.univ.id)
            session.add(usr)
            session.commit()
        except:
            # 重複ユーザはエラーが出ることを確認
            self.assertTrue(True)
            return
        self.assertTrue(False)
    
if __name__ == '__main__':
    unittest.main()
