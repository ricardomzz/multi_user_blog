from handler import *
import models.like
import models.post
from decorators import decorators


class Like(Handler):
    @decorators.require_login
    @decorators.post_exists
    @decorators.user_does_not_owns_post
    def get(self,post_id):

        post=models.post.Post.get_by_id(int(post_id))
        user=self.get_user()

        username=user.username
        if post.author.username == user.username:
            self.redirect("/")

        else:
            q=models.like.Like.all()
            q.filter("author =",user)
            q.filter("post =",post)
            like=q.get()

            if like:
                self.redirect("/")

            else:
                like=models.like.Like(post=post,author=user)
                like.put()
                post.put()
                self.redirect("/")
