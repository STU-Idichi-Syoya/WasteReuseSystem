from .models import Univercity, User
from . import db

def user_save(user_name,univercity_name,email_address,password1,birthday,univercity_id,db=db):
    univ=db.session.query(Univercity).filter_by(univercity_name=univercity_name).first()
    if univ is None:
        univ=Univercity(univercity_name=univercity_name.data)
        db.session.add(univ)
        db.session.commit()
    user_to_create = User(user_name=user_name.data,email_address=email_address.data,password=password1.data,birthday=birthday.data,univercity_id=univ.id)
    db.session.add(user_to_create)
    db.session.commit()
    
    return user_to_create