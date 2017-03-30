from handlers import tables, helper, Handler

class LoginHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(LoginHandler, self).__init__(*args, **kwargs)
        self.title = "Login"
        self.body_class = 'login-page'

    def get(self):
        if self.is_loggedin():
            self.redirect("/")
        else:
            self.render('login.jinja', handler=self, feedback=None)


    def post(self):
        if self.is_loggedin():
            self.redirect("/")
        else:
            username = self.request.get("username")
            password = self.request.get("password")
            error = {}

            user = tables.users.get(username=username)

            if not isinstance(user, tables.users.Users):
                error['username'] = "That user doesn't exists."
                error['password'] = " "
            elif helper.functions.hash_it(password=password, salt_it=False) != user.password:
                error['password'] = "That Isn't a valid password."

            if error :
                self.render('login.jinja', handler=self, feedback=True, error = error, username = username)
            else :
                self.login(username, user.password)
                self.redirect('/')
