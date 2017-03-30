from handlers import tables, helper, Handler

class BlogHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(BlogHandler, self).__init__(*args, **kwargs)
        self.body_class = "blog-page"

    def get(self):
        articles = tables.articles.get_all()
        self.render("blog.jinja", handler=self, articles=articles)
