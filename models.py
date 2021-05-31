from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
    
    db.app = app
    db.init_app(app)


class User(db.Model):

    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    image_url = db.Column(db.String(250), nullable=False, default="empty")


    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

