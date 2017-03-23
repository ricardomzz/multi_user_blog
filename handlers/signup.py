from handler import *

class SignUp(Handler):

    def get(self):

        self.render("userform.html",action="signup")

    def post(self):
        username=self.request.get('username')
        password=self.request.get('password')
        if self.username_exists(username):

            self.render("userform.html",action="signup",
            message="username already exists")
        else:
            user=User(username = username)
            user.userhash = user.make_pw_hash(password)
            user.put()
            self.render("userform.html",action="login",
            message="user created succesfully, please login")
