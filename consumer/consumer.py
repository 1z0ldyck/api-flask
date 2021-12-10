from dotenv import load_dotenv

import pika, os, json
import psycopg2
import consumer.config as config

class Consumer:

  config = {}
  
  def __init__(self):
    self.consumer_config = config.init_app(Consumer.config)
    self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.config['RABBITMQ_HOST']))
    self.channel = self.connection.channel()

  def receive_data(self):
    self.channel.basic_consume(queue='send_message',
                                 auto_ack=True,
                                 on_message_callback=self.publish_in_db)
    self.channel.start_consuming()
  
  @staticmethod
  def publish_in_db(ch, method, properties, data):
    data_dict = json.loads(data)
    conn_db = psycopg2.connect(host=Consumer.config['POSTGRES_HOST'], 
                               database=Consumer.config['POSTGRES_DATABASE'], 
                               user=Consumer.config['POSTGRES_USER'], 
                               password=Consumer.config['POSTGRES_PASSWORD'])
    cursor = conn_db.cursor()
    cursor.execute(f""" 
                   INSERT INTO People (name, age) VALUES ('{data_dict['name']}', {data_dict['age']})
                   """)
    conn_db.commit()
    
consumer = Consumer()
consumer.receive_data()