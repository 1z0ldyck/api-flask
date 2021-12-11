from flask_sqlalchemy import SQLAlchemy
from flask import Flask


def init_app(app):
    """Initialize database"""
    app.Database = Database(app)


class Database:

    db = SQLAlchemy()

    def __init__(self, app):
        self.database = self.db.init_app(app)
        with app.app_context():
            self.db.create_all()
