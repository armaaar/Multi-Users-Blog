from handlers import tables, helper, Handler
import re

class SignupHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(SignupHandler, self).__init__(*args, **kwargs)

    def get(self):
        if self.is_loggedin():
            self.redirect("/")
        else:
            self.render('signup.jinja', handler=self, feedback=None)

    def post(self):
        if self.is_loggedin():
            self.redirect("/")
        else:
            username = self.request.get("username")
            password = self.request.get("password")
            verify = self.request.get("verify")
            email = self.request.get("email")
            error = {}

            if not re.match("^[a-zA-Z0-9_-]{3,20}$", username):
                error['username'] = "That's not a valid username."

            if tables.users.user_exists(username=username):
                error['username'] = "That user already exists."

            if not re.match("^.{3,20}$", password):
                error['password'] = "That wasn't a valid password."
            elif password != verify :
                error['verify'] = "Your passwords didn't match."

            if not email or not re.match("^[\S]+@[\S]+.[\S]+$", email):
                error['email'] = "That's not a valid email."

            if error :
                self.render('signup.jinja', handler=self, feedback=True, error = error, username = username, email = email)
            else :
                password = helper.functions.hash_it(password=password, salt_it=False)
                tables.users.add(username=username, password=password, email=email)
                self.login(username, password)
                self.redirect('/')
