from handlers import tables, helper, Handler

class DeletePostHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(DeletePostHandler, self).__init__(*args, **kwargs)
        self.title = "Delete article"
        self.body_class = 'delarticle-page'

    def get(self, article_id):
        article= tables.articles.get(article_id)
        if self.is_loggedin() != article.user:
            self.page_redirect("/")
        else:
            self.render('delpost.jinja', handler=self, article=article)


    def post(self, article_id):
        article= tables.articles.get(article_id)
        if self.is_loggedin() != article.user:
            self.page_redirect("/")
        else:
            tables.articles.delete(article_id)
            self.page_redirect('/')
