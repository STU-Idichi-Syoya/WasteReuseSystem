from project.wrapper import user_save
import unittest
from .models import session


def test_flask(self):
  user = user_save(user_name="carlos", univercity_name="kandai", email_address="k3897@k.ac.jp",password1="0421",birthday=20000421, univercityId=self.univ.id)
  #user_name univercity_name email_address password1 birthday univercity_id
  session.add(user)
  session.commit()
  bu = session.query(user_save).all()
  self.assertEqual(len(bu),1)
  self.assertEqual(bu[0] ,user)

if __name__ == '__main__':
    unittest.main()