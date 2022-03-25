
from config import db
from blog.model import Blog
class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True, nullable=False)
    pword = db.Column(db.String(30), nullable=True)
    user_type = db.Column(db.Integer, default = 2)
    blogs = db.relationship(Blog, backref='user', lazy=True)

    
    def get(self):
        return {
            "user_id" : self.user_id,
            "user" : self.user,
            "name" : self.name,
            "email" : self.email,
            "user_type" : self.user_type
        }