import pika
import json
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='temp_queue')

while True:
    temp = round(random.uniform(20, 40), 2)
    data = json.dumps({"temperature": temp})
    channel.basic_publish(exchange='', routing_key='temp_queue', body=data)
    print(f"📤 Sent: {data}")
    time.sleep(2)

#Rabbit Mq -> http://localhost:15672
