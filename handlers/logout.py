from handler import *

class LogOut(Handler):
    def get(self):
        self.logout()
        self.redirect("/")
