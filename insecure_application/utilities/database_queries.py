
from config import db

def data_add(data_obj):
    db.session.add(data_obj)
    db.session.commit()