import pika
import psycopg2
import json

def callback(ch, method, properties, body):
    try:
        data = json.loads(body)
        temperature = data['temperature']
        conn = psycopg2.connect(
            dbname='sensor_db',
            user='postgres',
            password='your_password',
            host='localhost'
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO temperature_data(value) VALUES (%s)", (temperature,))
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Stored: {temperature}")
    except Exception as e:
        print(f"❌ Failed to insert: {e}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='temp_queue')
channel.basic_consume(queue='temp_queue', on_message_callback=callback, auto_ack=True)
print("📥 RabbitMQ consumer started.")
channel.start_consuming()
