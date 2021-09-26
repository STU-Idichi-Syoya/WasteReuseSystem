
from .wrapper import user_save
import unittest,csv


from . import create_app

app=create_app()
# session=db.session

class TestDB(unittest.TestCase):
  
  def test_register(self):
    # session=db.session
    with open(r"G:\WinDrive\resources - DB_sample_user.csv") as user:
        f=csv.DictReader(user)
        for i,u in enumerate(f):
            user_save(u["ユーザー名"],"東京美術大学", f"{i}@tokyo-art.ac.jp", "password1", 100000,icon="/user/"+u["image"])
    

if __name__ == '__main__':
    unittest.main()





