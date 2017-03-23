from handler import *
from models.post import Post 

class PostList(Handler):

    def get(self):
        posts=Post.all()
        posts.order('-created')
        self.render("postlist.html",posts=posts,
        username=self.get_username_from_cookie())
