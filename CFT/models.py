#pointint to app.py file and importing the db variable
from CFT import db, login_manager
from flask_login import UserMixin

#Flask extension that loads user id data -- directly from Flask documentation
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class WebText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    webpage = db.Column(db.String(150), unique=True, nullable=False)
    webtext = db.Column(db.String(10000), unique=True, nullable=False)

    def __repr__(self): #how our object is printed when we print
        return f"WebText('{self.webpage}', '{self.webtext}')"

#https://www.youtube.com/watch?v=cYWiDiIUxQc&t=647s
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self): #how our object is printed when we print
        return f"User('{self.username}', '{self.email}')"
