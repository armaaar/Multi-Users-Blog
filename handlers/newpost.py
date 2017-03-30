from handlers import tables, helper, Handler

class NewPostHandler(Handler):
    def __init__(self, *args, **kwargs) :
        super(NewPostHandler, self).__init__(*args, **kwargs)
        self.title = "Publish a new article"
        self.body_class = 'newpost-page'

    def get(self):
        if not self.is_loggedin():
            self.page_redirect("/")
        else:
            self.render('newpost.jinja', handler=self)

    def post(self):
        if not self.is_loggedin():
            self.page_redirect("/")
        else:
            title = elf.request.get("title")
            content = self.request.get("content")
            if not title:
                error = "Title must not be empty."
                self.render('newpost.jinja', handler=self, title = title, content = content, error = error)
            elif not content:
                error = "Content must not be empty."
                self.render('newpost.jinja', handler=self, title = title, content = content, error = error)
            else:
                article = tables.articles.add(title, content, self.get_cookie("username"))
                self.page_redirect("/article/"+str(article))
