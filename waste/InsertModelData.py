from .model import sqliteFile,User,Univercity,Item,ItemAllow,db
import os

def createTestTable(dev_test=False):
    if os.path.exists(sqliteFile):return
    db.create_all()
    print('creating...')
    session=db.session
    try:
        univ = Univercity(univercity_name="japan imperial Univ",domain_addr="abc.ac.jp")
        session.add(univ)
        session.commit()
        user = User(user_name="carlos", birthday=20000421, univercity_id=univ.id,email_address="test@abc.ac.jp", password="0421")
        session.add(user)
        session.commit()
        item=Item(user_id=user.id,item_name='testItem',category='実験',dangerous=False,need_credential="",expire=100000)
        session.add(item)
        session.commit()

        itemAllow=ItemAllow(item_id=item.id,allow_univercity_id=univ.id)
        session.add(itemAllow)
        session.commit()
    except:
        import traceback
        traceback.print_exc()
        
createTestTable()
        