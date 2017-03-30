from handlers import tables, helper, Handler

class ArticleHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(ArticleHandler, self).__init__(*args, **kwargs)
        self.body_class = 'article-page'

    def get(self, article_id):
        if not article_id.isdigit():
            self.redirect("/")
        else:
            article= tables.articles.get(article_id)
            self.render('article.jinja', handler=self, article= article)
