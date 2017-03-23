from handler import *
import models.comment
from decorators import decorators

class EditComment(Handler):

    @decorators.require_login
    @decorators.comment_exists
    @decorators.user_owns_comment
    def get(self,comment_id):

        comment=models.comment.Comment.get_by_id(int(comment_id))
        self.render("commentform.html",comment=comment,post=comment.post)

    @decorators.require_login
    @decorators.comment_exists
    @decorators.user_owns_comment
    def post(self,comment_id):
        comment=models.comment.Comment.get_by_id(int(comment_id))
        comment.content=self.request.get('content')
        comment.put()
        self.redirect("/")
