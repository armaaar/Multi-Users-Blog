from handlers import tables, helper, Handler
import time

class ArticleHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(ArticleHandler, self).__init__(*args, **kwargs)
        self.body_class = 'article-page'

    def get(self, article_id):
        if not article_id.isdigit():
            self.page_redirect("/")
        else:
            article= tables.articles.get(article_id)
            self.render('article.jinja', handler=self, article= article)

    def post(self, article_id):
        if not article_id.isdigit() or not self.is_loggedin():
            self.page_redirect("/")
        else:
            like = self.request.get("like")
            if like:
                username = self.get_cookie("username")
                if tables.likes.exist(article_id, username):
                    tables.likes.delete(article_id, username)
                else:
                    tables.likes.add(article_id, username)

                article= tables.articles.get(article_id)
                time.sleep(0.1) #sleep to get the right number of likes
                self.render('article.jinja', handler=self, article= article)
