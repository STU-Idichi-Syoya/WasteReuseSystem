from .model import User,session
import typing

def FindUserByMailAddrPasswd(mailAddr:str,passwd:str) ->typing.Union[User,None] :
    s=session
    usrs=s.query(User).filter_by(mailAddr=mailAddr,password=passwd).all()
    if len(usrs)!=1:
        return None
    return usrs[0]
    

def findByUserId(usrId):
    s=session
    return s.query(User).filter_by(id=usrId).first()