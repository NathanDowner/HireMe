from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

class UserForm(FlaskForm):
  fname = StringField('First Name', validators=[DataRequired()])
  lname = StringField('Last Name', validators=[DataRequired()])
  password  = PasswordField('Password', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  telephone = StringField('Telephone', validators=[DataRequired()])


class JobForm(FlaskForm):
  jTitle = StringField('Job Title', validators=[DataRequired()])
  JDesc = TextAreaField('Job Description', validators=[DataRequired()])
  category = SelectField('Category', validators=[DataRequired()])
  company = StringField('Company', validators=[DataRequired()])
  jLoc = StringField('Job Location', validators=[DataRequired()])