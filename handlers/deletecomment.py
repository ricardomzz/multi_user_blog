from handler import *
import models.comment


from decorators import decorators


class DeleteComment(Handler):
    @decorators.require_login
    @decorators.comment_exists
    @decorators.user_owns_comment
    def get(self,comment_id):
        comment=models.comment.Comment.get_by_id(int(comment_id))
        comment.delete()
        self.redirect("/")
