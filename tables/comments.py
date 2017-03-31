from tables import db
class Comments(db.Model):
    article = db.IntegerProperty(required= True)
    user = db.StringProperty(required= True)
    comment = db.TextProperty(required= True)
    submit_datetime = db.DateTimeProperty(auto_now_add = True)

def get(comment_id):
    if str(comment_id).isdigit():
        comment = db.GqlQuery("SELECT * FROM Comments WHERE __key__ = KEY('Comments', :comment_id) LIMIT 1", comment_id=long(comment_id))

    if 'comment' in locals() and isinstance(comment.get(), Comments):
        return comment[0]
    return None

def get_comments(article_id=None, order="DESC"):
    if order != "DESC":
        order= "ASC"
    else:
        order= "DESC"
    if str(article_id).isdigit():
        comments = db.GqlQuery("SELECT * FROM Comments WHERE article= :article_id ORDER BY submit_datetime %s " % order, article_id=long(article_id))

    if 'comments' in locals() and isinstance(comments.get(), Comments):
        return comments.fetch(limit=None)
    return None

def add(article_id, username, comment):
    comment = Comments(article = long(article_id), user=username, comment=comment)
    comment.put()
    return comment.key().id()

def edit(comment_id, comment):
    if comment_id.isdigit():
        com = get(comment_id)
        com.comment = comment
        com.put()
        return True
    else:
        return None

def delete(comment_id):
    if comment_id.isdigit():
        comment = get(comment_id)
        comment.delete()
        return True
    else:
        return None
