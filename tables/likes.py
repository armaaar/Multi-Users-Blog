from tables import db
class Likes(db.Model):
    article = db.IntegerProperty(required= True)
    user = db.StringProperty(required= True)

def exist(article_id, username):
    if str(article_id).isdigit():
        likes = db.GqlQuery("SELECT * FROM Likes WHERE article=:article_id AND user=:username", article_id=int(article_id), username=str(username))

    if 'likes' in locals() and isinstance(likes.get(), Likes):
        return likes[0]
    return None

def get_likes(article_id=None):
    if str(article_id).isdigit():
        likes = db.GqlQuery("SELECT * FROM Likes WHERE article= :article_id", article_id=int(article_id))

    if 'likes' in locals() and isinstance(likes.get(), Likes):
        return len(likes.fetch(limit=None))
    return 0

def add(article_id, username):
    like = Likes(article = long(article_id), user=username)
    like.put()
    return like.key().id()

def delete(article_id, user):
    if article_id.isdigit():
        like = exist(article_id, user)
        like.delete()
        return True
    else:
        return None
