from dotenv import load_dotenv
import os

def init_app(consumer):
  """Configuration of Consumer application"""
  load_dotenv()
  consumer.config['RABBITMQ_HOST'] = os.environ['RABBITMQ_HOST'] 
  consumer.config['POSTGRES_HOST'] = os.environ['POSTGRES_HOST']
  consumer.config['POSTGRES_USER'] = os.environ['POSTGRES_USER']
  consumer.config['POSTGRES_PASSWORD'] = os.environ['POSTGRES_PASSWORD']
  
  