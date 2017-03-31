from handlers import tables, helper

# webapp
import webapp2
# Templates
import os
import jinja2
# Other
import time

# Load Templates
templates_dir = os.path.join(os.path.dirname(__file__), helper.variables.templates_dir)
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(templates_dir),
                         autoescape = True)



class Handler(webapp2.RequestHandler):

    def __init__(self, *args, **kwargs) :
        super(Handler, self).__init__(*args, **kwargs)
        self.title = helper.variables.site_title
        self.body_class = helper.variables.body_class
        self.description = helper.variables.description
        self.keywords = helper.variables.keywords
        self.seo_img = helper.variables.seo_img

    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **args):
        t = jinja_env.get_template(template)
        return t.render(args, helper=helper, tables=tables)

    def render(self, template, **args):
        self.write( self.render_str(template, **args) )

    def set_cookie(self, name, value):
        #self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/' % (str(name), str(value)))
        self.response.set_cookie(str(name), str(value))
        return True
    def get_cookie(self, name):
        return self.request.cookies.get(name)

    def delete_cookie(self, name):
        self.response.delete_cookie(name)
        return True

    def is_loggedin(self):
        cookie_username = self.get_cookie('username')
        cookie_pw = self.get_cookie('pw')
        user = tables.users.get(username=cookie_username)

        if isinstance(user, tables.users.Users):
            cookie_pw = cookie_pw.split("|")
            if cookie_pw[0] == helper.functions.hash_it(user.password, cookie_pw[1]):
                return cookie_username

        return None

    def login(self, username, password):
        if not self.is_loggedin():
            self.set_cookie("username", username)
            salt = helper.functions.create_salt()
            password = "%s|%s" % (helper.functions.hash_it(password, salt), salt)
            self.set_cookie("pw", password)
            return True
        return True

    def page_redirect(self, url):
        time.sleep(0.1) #sleep to have enough time setting cookies or change db or whatever
        self.redirect(str(url))
