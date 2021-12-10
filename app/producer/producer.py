import pika, os, json
from dotenv import load_dotenv

class Producer:
  def __init__(self):
    load_dotenv()
    self.connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['RABBITMQ_HOST']))
    self.channel = self.connection.channel()
  
  def publish_data(self, message):
    self.channel.queue_declare(queue='send_message')
    self.channel.basic_publish(exchange='',
                               routing_key='send_message',
                               body=message
                               )
    
    