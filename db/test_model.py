from model import session
from model import  Univercity, User,createTable,deleteTable
import unittest
# from model import User, Univercity, session

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
      createTable()
      univ = Univercity(univercityName="japan imperial Univ", domainAddr="imperial.ac.jp")
      session.add(univ)
      session.commit()

    def tearDown(self):
      deleteTable()


    def InsertUserTest(self):
        # Test feature one.
        univ = session.query(Univercity).filter(Univercity.univercityName=="japan imperial Univ").first()
        user = User(name="carlos", birthday=20000421, univercityId=univ.id, mailAddr="k3897@k.ac.jp", password="0421")
        session.add(univ)
        session.commit()
        bu=session.query(User).all().first()
        unittest.assertTrue(bu==user)
    # def test_feature_two(self):
    #     # Test feature two.
    #     pass

if __name__ == '__main__':
    unittest.main()
