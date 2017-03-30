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
