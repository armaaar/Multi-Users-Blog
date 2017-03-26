import handlers

class Handler(handlers.webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **args):
        t = handlers.jinja_env.get_template(template)
        return t.render(args)

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
        user = users.get(username=cookie_username)

        if isinstance(user, Users):
            cookie_pw = cookie_pw.split("|")
            if cookie_pw[0] == helper.functions.hash_it(user.password, cookie_pw[1]):
                return True

        return None

    def login(self, username, password):
        if not self.is_loggedin():
            self.set_cookie("username", username)
            salt = helper.functions.create_salt()
            password = "%s|%s" % (helper.functions.hash_it(password, salt), salt)
            self.set_cookie("pw", password)
            handlers.time.sleep(0.1)
            return True
        return True
