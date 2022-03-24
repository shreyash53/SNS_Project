

from config import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(30), unique=True, nullable=True)
    name = db.Column(db.String(30))
    pword = db.Column(db.String(30), nullable=True)
    user_type = db.Column(db.Integer, default = 2)
    
    def get(self):
        return {
            "user_id" : self.user_id,
            "user" : self.user,
            "name" : self.name,
            "user_type" : self.user_type
        }