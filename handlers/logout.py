from handlers import tables, helper, Handler

class LogoutHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(LogoutHandler, self).__init__(*args, **kwargs)

    def get(self):
        self.delete_cookie('username')
        self.redirect("/")
