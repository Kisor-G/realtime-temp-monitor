from fastapi import FastAPI, WebSocket
import pika
import threading
import asyncio
import json
import psycopg2

app = FastAPI()
clients = set()

def get_pg_conn():
    return psycopg2.connect(
        dbname='sensor_db',
        user='postgres',
        password='your_password',
        host='localhost'
    )

def save_to_postgres(temp):
    try:
        conn = get_pg_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO temperature_data (value, timestamp) VALUES (%s, NOW())", (temp,))
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Saved {temp} to PostgreSQL")
    except Exception as e:
        print(f"❌ Error saving to PostgreSQL: {e}")

async def broadcast(message):
    disconnected = set()
    for ws in clients:
        try:
            await ws.send_json(message)
        except:
            disconnected.add(ws)
    clients.difference_update(disconnected)

def rabbitmq_listener():
    def callback(ch, method, properties, body):
        data = json.loads(body)
        print(f"📡 Received: {data}")
        save_to_postgres(data['temperature'])
        asyncio.run(broadcast(data))

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='temp_queue')
    channel.basic_consume(queue='temp_queue', on_message_callback=callback, auto_ack=True)
    print("📡 RabbitMQ listener started.")
    channel.start_consuming()

@app.on_event("startup")
def start_listener():
    threading.Thread(target=rabbitmq_listener, daemon=True).start()

@app.websocket("/ws/temperature")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except:
        clients.remove(websocket)
