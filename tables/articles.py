from tables import db
class Articles(db.Model):
    title = db.StringProperty(required= True)
    content = db.TextProperty(required= True)
    user = db.StringProperty(required= True)
    creation_date = db.DateTimeProperty(auto_now_add = True)

def get_all(order="DESC", limit=None):
    if order != "DESC":
        order= "ASC"
    else:
        order= "DESC"
    return db.GqlQuery("SELECT * FROM Articles ORDER BY creation_date %s" % order).fetch(limit=limit)

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

def edit(article_id, title, content):
    if article_id.isdigit():
        article = get(article_id)
        article.title = title
        article.content = content
        article.put()
        return True
    else:
        return None

def delete(article_id):
    if article_id.isdigit():
        article = get(article_id)
        article.delete()
        return True
    else:
        return None

def Delete_all():
    articles = Articles.all()
    for u in articles:
        u.delete()
