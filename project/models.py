from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    def __init__(self, name, company_id):
        self.name = name
        self.company_id = company_id

    @property
    def serialize(self):
        return {'id': self.id, 'name': self.name, 'company_id': self.company_id, 'admin': self.admin}
        
    def __repr__(self):
        return f'<User {self.name}>'

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(), nullable=False)
    company_city = db.Column(db.String(), nullable=False)
    company_address = db.Column(db.String())
    company_revenue = db.Column(db.Numeric(decimal_return_scale=2))
    users = db.relationship('User', backref='company', lazy=True)

    def __init__(self, company_name, company_city, **kwargs):
        self.company_name = company_name
        self.company_city = company_city
        super(Company, self).__init__(**kwargs)
    
    @property
    def serialize(self):
        return {'id': self.id, 'company_name': self.company_name, 'company_city': self.company_city, 'company_address': self.company_address, 'company_revenue': str(self.company_revenue)}

    def __repr__(self):
        return f'<Company {self.company_name}'
