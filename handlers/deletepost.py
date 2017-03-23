from handler import *
import models.post
from decorators import decorators

class DeletePost(Handler):

    @decorators.require_login
    @decorators.post_exists
    @decorators.user_owns_post
    def get(self,post_id):

        post=models.post.Post.get_by_id(int(post_id))
        post.delete()
        self.redirect("/")
