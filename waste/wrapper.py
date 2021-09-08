from sqlalchemy.sql.operators import all_op
from .model import ItemAllow, User,session,Item
import typing

def FindUserByMailAddrPasswd(email_address:str,passwd:str) ->typing.Union[User,None] :
    s=session
    usrs = s.query(User).filter_by(email_address=email_address, password=passwd).all()
    if len(usrs)!=1:
        return None
    return usrs[0]

def findByUserId(usrId):
    s=session
    return s.query(User).filter_by(id=usrId).first()

def findAll():
    return session.query(User).all()


def session_add(user_to_create):
    session_add(user_to_create)
    session.commit()
    
def findItemByWord(searchWord:str,userId:int=None):
    # ログインしていない場合の検索は．．．？
    if userId==None:
        return []

    return session.query(Item,User,ItemAllow).filter(Item.id==ItemAllow.item_id,
        Item.user_id==userId,Item.item_name.like(searchWord)).all()
    
