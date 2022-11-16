from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
   id = db.Column(db.Integer(), primary_key=True)
   short_name = db.Column(db.Text(), nullable=False)
   long_name = db.Column(db.Text(), nullable=False)
   age =  db.Column(db.Integer(), nullable=False)
   dob= db.Column(db.Text(), nullable=False)
   height_cm = db.Column(db.Integer(), nullable=False)
   weight_kg = db.Column(db.Integer(), nullable=False)
   nationality = db.Column(db.Text(), nullable=False)
   club_joined = db.Column(db.Text(), nullable=False)

   def to_dict(self):
       return{
           'name': self.name,
           'height': self.height,
           'weight': self.weight
       }
