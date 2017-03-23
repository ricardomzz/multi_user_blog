from google.appengine.ext import db
from models.post import Post
from models.user import User

class Like(db.Model):
    post = db.ReferenceProperty(Post,collection_name='likes',required = True)
    author = db.ReferenceProperty(User,collection_name='likes',required = True)
