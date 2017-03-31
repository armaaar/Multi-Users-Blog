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
            comments= tables.comments.get_comments(article_id)
            self.render('article.jinja', handler=self, article= article, comments=comments)

    def post(self, article_id):
        if not article_id.isdigit() or not self.is_loggedin():
            self.page_redirect("/")
        else:

            like = self.request.get("like")
            new_comment = self.request.get("new-comment")
            delete_comment = self.request.get("delete-comment")
            edit_comment = self.request.get("edit-comment")

            if like:
                username = self.get_cookie("username")
                if tables.likes.exist(article_id, username):
                    tables.likes.delete(article_id, username)
                else:
                    tables.likes.add(article_id, username)
                self.page_redirect("/article/%s/#like" % article_id)

            elif new_comment:
                new_comment = self.request.get("comment")
                username = self.get_cookie("username")
                tables.comments.add(article_id, username, new_comment)
                self.page_redirect("/article/%s/#comments" % article_id)

            elif delete_comment:
                comment_id = self.request.get("comment-id")
                tables.comments.delete(comment_id)
                self.page_redirect("/article/%s/#comments" % article_id)

            elif edit_comment:
                comment_id = self.request.get("comment-id")
                comment = self.request.get("comment")
                tables.comments.edit(comment_id, comment)
                self.page_redirect("/article/%s/#comments" % article_id)
            else:
                self.page_redirect("/article/%s/" % article_id)
