from functools import wraps
import models.comment
import models.post
import models.user

def comment_exists(function):
    @wraps(function)
    def wrapper(self,comment_id):
        comment=models.comment.Comment.get_by_id(int(comment_id))
        if comment:
            return function(self,comment_id)
        else:
            return self.error(404)
    return wrapper

def post_exists(function):
    @wraps(function)
    def wrapper(self,post_id):
        comment=models.post.Post.get_by_id(int(post_id))
        if comment:
            return function(self,post_id)
        else:
            return self.error(404)
    return wrapper

def require_login(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        cookie_username = args[0].get_secure_val(args[0].request.cookies.get('username'))
        if cookie_username:
            return function(*args,**kwargs)
        else:
            return args[0].redirect("/login")
    return wrapper

def user_owns_post(function):
    @wraps(function)
    def wrapper(self,post_id):
        user=self.get_user()
        post=models.post.Post.get_by_id(int(post_id))
        if user.username == post.author.username:
            return function(self,post_id)
        else:
            return self.error(403)
    return wrapper

def user_owns_comment(function):
    @wraps(function)
    def wrapper(self,comment_id):
        user=self.get_user()
        comment=models.comment.Comment.get_by_id(int(comment_id))
        if user.username == comment.author.username:
            return function(self,comment_id)
        else:
            return self.error(403)
    return wrapper

def user_does_not_owns_post(function):
    @wraps(function)
    def wrapper(self,post_id):
        user=self.get_user()
        post=models.post.Post.get_by_id(int(post_id))
        if user.username != post.author.username:
            return function(self,post_id)
        else:
            return self.error(403)
    return wrapper
