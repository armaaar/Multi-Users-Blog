from handlers import tables, helper, Handler

class IndexHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(IndexHandler, self).__init__(*args, **kwargs)

    def get(self):
        self.render("blog.jinja", handler=self)
