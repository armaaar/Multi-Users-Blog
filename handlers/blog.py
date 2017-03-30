from handlers import tables, helper, Handler

class BlogHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(BlogHandler, self).__init__(*args, **kwargs)

    def get(self):
        articles = tables.articles.get_all()
        self.render("blog.jinja", handler=self, articles=articles)
