from google.appengine.ext import db
from models.user import User
from models.post import Post
import random
import string

class Comment(db.Model):
    content = db.TextProperty(required = True)
    author = db.ReferenceProperty(User,collection_name='comments',
    required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    modified = db.DateTimeProperty(auto_now=True)
    post = db.ReferenceProperty(Post,collection_name='comments',required = True)
    url=db.StringProperty()

    @property
    def url(self):
        return self.key().id()
