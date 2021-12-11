from app.ext.db import (
    Database
)


class People(Database.db.Model):
    id = Database.db.Column(Database.db.Integer, primary_key=True)
    name = Database.db.Column(Database.db.String(25), nullable=False)
    age = Database.db.Column(Database.db.Integer, nullable=False)

    def to_json(self):
        return {
            "name": self.name,
            "age": int(self.age)
        }
