from tables import db
class Users(db.Model):
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.EmailProperty(required = True)
    signup_datetime = db.DateTimeProperty(auto_now_add = True)
    lastlogin_datetime = db.DateTimeProperty(auto_now_add = True)


def get(username=None, user_id=None):
    if user_id:
        user = db.GqlQuery("SELECT * FROM Users WHERE __key__ = KEY('Users', :user_id) LIMIT 1", user_id=int(user_id))
    elif username:
        user = db.GqlQuery("SELECT * FROM Users WHERE username = :username LIMIT 1", username=str(username))
    if 'user' in locals() and isinstance(user.get(), Users):
        return user[0]
    return None

def user_exists(username=None, user_id=None):
    user = User.get(username, user_id)
    if isinstance(user, Users):
        return True
    return None

def add(username, password, email):
    if not User.get(username=username):
        user = Users(username = username, password = password, email = email)
        user.put()
        return True
    return None

def Delete_all():
    users = Users.all()
    for u in users:
        u.delete()
