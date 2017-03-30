from handlers import tables, helper, Handler

class EditPostHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(EditPostHandler, self).__init__(*args, **kwargs)
        self.title = "Edit article"
        self.body_class = 'editpost-page'

    def get(self, article_id):
        article= tables.articles.get(article_id)
        if self.is_loggedin() != article.user:
            self.page_redirect("/login/")
        else:
            self.render('newpost.jinja', handler=self, article_id= article_id, title = article.title, content = article.content)

    def post(self, article_id):
        article= tables.articles.get(article_id)
        if self.is_loggedin() != article.user:
            self.page_redirect("/login/")
        else:
            title = self.request.get("title")
            content = self.request.get("content")

            if not title:
                error = "Title must not be empty."
                self.render('newpost.jinja', handler=self, article_id= article_id, title = title, content = content, error = error)
            elif not content:
                error = "Content must not be empty."
                self.render('newpost.jinja', handler=self, article_id= article_id, title = title, content = content, error = error)
            else:
                article = tables.articles.edit(article_id, title, content)
                self.page_redirect("/article/%s" % str(article_id))
