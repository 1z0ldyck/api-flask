from app.ext.db import db

class People(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(25), nullable=False) 
   age = db.Column(db.Integer, nullable=False)
   
   def to_json(self):
       return {
           "name": self.name,
           "age": int(self.age)
       }
       
