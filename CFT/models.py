#pointint to app.py file and importing the db variable
from CFT import db, login_manager
from flask_login import UserMixin

#Flask extension that loads user id data -- directly from Flask documentation
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#https://www.youtube.com/watch?v=cYWiDiIUxQc&t=647s
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    #relationship (an addition query, NOT a column) between User and Post models (user can have multiple posts)
    #backref = the author attribute
    #lazy = loads the data from the database
    #posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self): #how our object is printed when we print
        return f"User('{self.username}', '{self.email}')"
