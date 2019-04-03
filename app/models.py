# id, fname, lname, pass, tele, email, date_joined
from . import db

class User(db.Model):
  __tablename__ = 'Users'
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(80))
  lastname = db.Column(db.String(80))
  password = db.Column(db.String(256))
  telephone = db.Column(db.String(12))
  email = db.Column(db.String(80), unique=True)
  date_joined = db.Column(db.DateTime)

  def __init__(self, fname, lname, password, tele, email, date):
    self.firstname = fname
    self.lastname = lname
    self.password = password
    self.telephone = tele
    self.email = email
    self.date_joined = date

  def __repr__(self):
    return '<User {} {}>'.format(self.firstname, self.lastname)

class Job(db.Model):
  __tablename__ = 'Jobs'

  id = db.Column(db.Integer, primary_key=True)
  job_title = db.Column(db.String(80))
  job_description = db.Column(db.String(500))
  category = db.Column(db.String(80))
  company_name = db.Column(db.String(80))
  company_location = db.Column(db.String(255))
  date_posted = db.Column(db.DateTime)

  def __init__(self, jTitle, jDesc, category, cName, cLoc, date):
    self.job_title = jTitle
    self.job_description = jDesc
    self.category = category
    self.company_name = cName
    self.company_location = cLoc
    self.date_posted = date

  def __repr__(self):
    return '<Job {}>'.format(self.id)


# class JobAppliedFor(db.Model):

#   __tablename__ = 'Jobs Applied For'

#   id  = db.Column(db.Integer)
#   job_id = db.Column(db.Integer)
#   user_id = db.relationship('User', backref='')