
from config import db

def data_add(data_obj):
    db.session.add(data_obj)
    db.session.commit()
    
def data_delete(data_model):
    db.session.query(data_model).delete()
    db.session.commit()