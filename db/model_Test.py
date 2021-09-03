import unittest
from test import support
# from model import User, Univercity, session
import model

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
      univ = Univercity(univercityName="japan imperial Univ", domainAddr="imperial.ac.jp")
      session.add(univ)
      session.commit()

    def tearDown(self):
      pass

    def test_feature_one(self):
        # Test feature one.
        univ = session.query(Univercity).filter(univ="japan imperial Univ").get(1)
        user = User(name="carlos", birthday=20000421, univercityId=univ.id, mailAddr="k3897@k.ac.jp", password="0421")
        session.add(univ)
        session.commit()

    def test_feature_two(self):
        # Test feature two.
        pass

if __name__ == '__main__':
    unittest.main()
