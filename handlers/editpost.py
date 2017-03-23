from handler import *
import models.post
import models.comment
from decorators import decorators

class EditPost(Handler):
    @decorators.require_login
    @decorators.post_exists
    @decorators.user_owns_post
    def get(self,post_id):

        post=models.post.Post.get_by_id(int(post_id))
        self.render("postform.html",post=post)

    @decorators.require_login
    @decorators.post_exists
    @decorators.user_owns_post
    def post(self,post_id):
        comment=models.comment.Comment.get_by_id(int(post_id))
        post=models.post.Post.get_by_id(int(post_id))
        post.content=self.request.get('content')
        post.title=self.request.get('title')
        post.put()
        self.redirect("/")
