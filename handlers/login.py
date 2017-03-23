from handler import *

class Login(Handler):

    def get(self):

        self.render("userform.html",action="login")

    def post(self):
        username=self.request.get('username')
        password=self.request.get('password')
        if self.username_exists(username):
            user=self.get_user_by_username(username)
            if user.authenticate(password):
                self.login(username,password)
                self.redirect("/")
            else:
                self.render("userform.html",action="login",
                message="wrong password")
        else:
            self.render("userform.html",action="login",
            message="username does not exist")
