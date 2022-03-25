from config import db

class Blog(db.Model):
    blog_id = db.Column(db.Integer, primary_key = True)
    blog_title = db.Column(db.String(100), nullable=False)
    blog_content = db.Column(db.String(4000), nullable=False)
    blog_user = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    modified_time = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def get(self):
        return {
            "blog_id" : self.blog_id,
            "blog_title" : self.blog_title,
            "blog_content" : self.blog_content,
        }