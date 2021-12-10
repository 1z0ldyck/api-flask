import pika, os, json
from dotenv import load_dotenv
import psycopg2

class Consumer:
  def __init__(self):
    load_dotenv()
    self.connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['RABBITMQ_HOST']))
    self.channel = self.connection.channel()

  def receive_data(self):
    self.channel.basic_consume(queue='send_message',
                                 auto_ack=True,
                                 on_message_callback=self.publish_in_db)
    self.channel.start_consuming()
  
  @staticmethod
  def publish_in_db(ch, method, properties, data):
    data_dict = json.loads(data)
    conn_db = psycopg2.connect(host=os.environ['POSTGRES_HOST'], database=os.environ['POSTGRES_DATABASE'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])
    cursor = conn_db.cursor()
    cursor.execute(f""" 
                   INSERT INTO People (name, age) VALUES ('{data_dict['name']}', {data_dict['age']})
                   """)
    conn_db.commit()
    
consumer = Consumer()
consumer.receive_data()