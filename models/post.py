from google.appengine.ext import db
from models.user import User


import random
import string


class Post(db.Model):
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    author = db.ReferenceProperty(User,collection_name='posts', required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    modified = db.DateTimeProperty(auto_now=True)





    @property
    def url(self):
        return self.key().id()


    @property
    def count_likes(self):
        count=self.likes.count()
        return count
