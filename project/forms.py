from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, DecimalField
from wtforms.validators import DataRequired, EqualTo


class CreateUser(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    company_id = SelectField('Company ID', coerce=int, validators=[DataRequired()])

class UpdateUser(FlaskForm):
    name = StringField('Name')
    company_id = SelectField('Company', coerce=int)

class CreateCompany(FlaskForm):
    company_name = StringField('*Name', validators=[DataRequired()])
    company_city = StringField('*City', validators=[DataRequired()])
    company_address = StringField('Address', default='')
    company_revenue = DecimalField('Revenue', places=2, default=0)

class UpdateCompany(FlaskForm):
    company_name = StringField('Name', default='')
    company_city = StringField('City', default='')
    company_address = StringField('Address', default='')
    company_revenue = DecimalField('Revenue')