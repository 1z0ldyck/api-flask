import pika
import json
import psycopg2
import config as config


class Consumer:
    """Application with the consumption proposal as application messages through the RabbitMQ queue"""
    config = {}

    def __init__(self):
        self.consumer_config = config.init_app(Consumer)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.config['RABBITMQ_HOST']))
        self.channel = self.connection.channel()

    def receive_data(self):
        """Consumes data from the RabbitMQ queue"""
        self.channel.basic_consume(queue='send_message',
                                   auto_ack=True,
                                   on_message_callback=self.publish_in_db)
        self.channel.start_consuming()
        
    @staticmethod
    def convert_str_to_int(values):
      for value in values:
        if not value.isalpha():
          value = int(value)

    @staticmethod
    def publish_in_db(ch, method, properties, data):
        """Publish the consumed data to the database"""
        queue_data = list(json.loads(data).items())

        conn_db = psycopg2.connect(host=Consumer.config['POSTGRES_HOST'],
                                   database=Consumer.config['POSTGRES_DATABASE'],
                                   user=Consumer.config['POSTGRES_USER'],
                                   password=Consumer.config['POSTGRES_PASSWORD'])
        cursor = conn_db.cursor()
        for column, values in queue_data:
            k, v = list(values.keys()), list(values.values())
            cursor.execute(f""" 
                    INSERT INTO {column} ({','.join(str(x) for x in k)}) VALUES ({(','.join("'" + str(x) + "'" for x in v))})
                    """)
            conn_db.commit()
          
          
consumer = Consumer()
consumer.receive_data()
