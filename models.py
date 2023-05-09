"""Models for pet adoption."""
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy import text 

db = SQLAlchemy()

def connect_db(app):
        db.init_app(app)


class Cupcake(db.Model):
        """Delicious Cupcakes"""

        __tablename__ = 'cupcakes'
        
        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        flavor =  db.Column(db.String(50),nullable = False)
        size = db.Column(db.String(50),nullable = False)
        rating = db.Column(db.Float)
        image = db.Column(db.String(200), nullable = True, default="https://tinyurl.com/demo-cupcake")

