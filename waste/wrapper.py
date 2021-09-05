from .model import User,session
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