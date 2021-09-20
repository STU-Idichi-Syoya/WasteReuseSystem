from .models import Univercity, User
from . import db
from project.models import Item

def user_save(user_name,univercity_name,email_address,password1,birthday,db=db):
    univ=db.session.query(Univercity).filter_by(univercity_name=univercity_name).first()
    if univ is None:
        univ=Univercity(univercity_name=univercity_name)
        db.session.add(univ)
        # db.session.commit()
        db.session.flush()
    user_to_create = User(user_name=user_name,email_address=email_address,birthday=birthday,univercity_id=univ.id)
    user_to_create.password=password1
    db.session.add(user_to_create)
    db.session.commit()
    
    return user_to_create

def item_buy(item_id):
    item = db.session.query(Item).filter_by(id=item_id)
    if item is not None:
        item.is_active = False
        db.session.commit()


