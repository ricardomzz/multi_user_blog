from handler import *
import models.comment
import models.post
from decorators import decorators

class Comment(Handler):
    @decorators.require_login
    @decorators.post_exists
    def get(self,post_id):
        post=models.post.Post.get_by_id(int(post_id))
        user=self.get_user()
        self.render("commentform.html",post=post,user=user)

    @decorators.require_login
    @decorators.post_exists
    def post(self,post_id):
        user=self.get_user()
        content=self.request.get('content')
        post=models.post.Post.get_by_id(int(post_id))
        comment=models.comment.Comment(author=user,post=post,content=content)
        comment.put()
        self.redirect("/")
