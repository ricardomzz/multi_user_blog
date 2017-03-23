import os
import webapp2
import hmac
import jinja2
from models.user import User

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

SECRET="SECRET_STRING"




class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a,**kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def hash_str(self,str):
        return hmac.new(SECRET,str).hexdigest()

    def make_secure_val(self,str):
        return "%s|%s" % (str,self.hash_str(str))

    def get_secure_val(self,h):

        val=h.split("|")[0]
        if h == self.make_secure_val(val):
            return val

    def set_username(self,user):
        username=user.username

        self.response.headers.add_header(
        'Set-Cookie',str('username=%s' % self.make_secure_val(username)))

    def get_username_from_cookie(self):
        if 'username' in self.request.cookies:

            cookie_username = self.get_secure_val(
            self.request.cookies.get('username'))

            return cookie_username


    def username_exists(self,username):
        q=User.all()
        q.filter("username =",username)
        user=q.get()
        if user:
            return True
        else:
            return False

    def get_user_by_username(self,username):
        q=User.all()
        q.filter("username =",username)
        user=q.get()
        return user





    def login(self,username,password):
        user=self.get_user_by_username(username)
        user.authenticate(password)
        self.set_username(user)

    def is_logged_in(self):
        session_username=self.get_username_from_cookie()
        return self.username_exists(session_username)



    def logout(self):
        self.response.headers.add_header('Set-Cookie',str('username=""'))

    def get_user(self):
        return self.get_user_by_username(self.get_username_from_cookie())
