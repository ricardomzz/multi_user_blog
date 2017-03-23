from handler import *
from models.post import Post
from decorators import decorators

class NewPost(Handler):

    @decorators.require_login
    def get(self):
        user=self.get_user()
        if self.is_logged_in():
            self.render("postform.html",user=user)
        else:
            self.redirect("/login")

    @decorators.require_login
    def post(self):
        user=self.get_user()
        content=self.request.get('content')
        title=self.request.get('title')

        post=Post(author=user,content=content,title=title,num_likes=0)
        post.put()

        self.redirect("/")
