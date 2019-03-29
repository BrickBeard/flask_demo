from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo


class CreateUser(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Name"})
    company = StringField('Company', validators=[DataRequired()], render_kw={"placeholder": "Company"})
    city = StringField('City', validators=[DataRequired()], render_kw={"placeholder": "City"})

class UpdateUser(FlaskForm):
    name = StringField('Name')
    company = StringField('Company')
    city = StringField('City')