from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
  """Initialize database"""
  app.Database = db.init_app(app)