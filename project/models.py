from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    company = db.Column(db.String())
    city = db.Column(db.String())
    admin = db.Column(db.Boolean)

    def __init__(self, name, company, city):
        self.name = name
        self.company = company
        self.city = city

    @property
    def serialize(self):
        return {'id': self.id, 'name': self.name, 'company': self.company, 'city': self.city, 'admin': self.admin}
        
    def __repr__(self):
        return f'<User {self.name}>'