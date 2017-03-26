from tables import db
class Articles(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    date = db.DateProperty(auto_now_add = True)
