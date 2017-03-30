from tables import db
class Articles(db.Model):
    title = db.StringProperty(required= True)
    content = db.TextProperty(required= True)
    user = db.StringProperty(required= True)
    date = db.DateProperty(auto_now_add = True)

def get_all(order="DESC"):
    if order != "DESC":
        order= "ASC"
    else:
        order= "DESC"
    return db.GqlQuery("SELECT * FROM Articles ORDER BY date %s" % order).fetch(limit=None)

def get(article_id=None):
    if article_id.isdigit():
        article = db.GqlQuery("SELECT * FROM Articles WHERE __key__ = KEY('Articles', :article_id) LIMIT 1", article_id=int(article_id))

    if 'article' in locals() and isinstance(article.get(), Articles):
        return article[0]
    return None

def add(title, content, username):
    article = Articles(title = title, content = content, user=username)
    article.put()
    return article.key().id()

def Delete_all():
    users = Users.all()
    for u in users:
        u.delete()
