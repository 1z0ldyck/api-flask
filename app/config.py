import os
from dotenv import load_dotenv

def init_app(app):
  load_dotenv()
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['POSTGRESQL_URL']
  app.config['RABBITMQ_HOST'] = os.environ['RABBITMQ_HOST']
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False