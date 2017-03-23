from google.appengine.ext import db
import hashlib
import random
import string

class User(db.Model):
    username = db.StringProperty(required = True)
    userhash = db.StringProperty()
    salt = db.StringProperty()

    def __make_salt(self):
        return ''.join(random.choice(string.letters) for x in xrange(5))

    def make_pw_hash(self,password):
        if not self.salt:
            self.salt = self.__make_salt()
        h = hashlib.sha256(password+self.salt).hexdigest()
        return h

    def authenticate(self, password):
        return self.make_pw_hash(password) == self.userhash
