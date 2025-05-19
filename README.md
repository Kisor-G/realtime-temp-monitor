# RTA on Temperature Monitoring
This project simulates a temperature sensor that publishes data to RabbitMQ, processes it through a consumer that stores it in PostgreSQL, and broadcasts it in real time to connected WebSocket clients via a FastAPI backend.

# 🌡️ Real-Time Temperature Streaming with RabbitMQ, PostgreSQL & FastAPI

This project simulates a temperature sensor that streams data through RabbitMQ, stores it in PostgreSQL, and serves real-time updates to clients using FastAPI + WebSocket.

## 📦 Tech Stack
- **Python**
- **RabbitMQ**
- **PostgreSQL**
- **FastAPI** (with WebSocket)
- **Pika** (for RabbitMQ)
- **psycopg2** (for PostgreSQL)

## 📁 Project Structure

producer/ -> Sends random temperature data to RabbitMQ
consumer/ -> Reads data from RabbitMQ and inserts into PostgreSQL
db/ -> Database setup script

## 🚀 Getting Started

1. **Install RabbitMQ & PostgreSQL locally**
2. **Clone this repo**

git clone 
cd temperature-streaming

Install dependencies

pip install -r requirements.txt

Run DB Setup

python db_setup.py

Start the Producer

python producer.py

Start FastAPI WebSocket App

uvicorn app.main:app --reload

Open WebSocket connection
Use any WebSocket client (e.g., browser, Postman, custom frontend) to connect to:

ws://localhost:8000/ws/temperature
