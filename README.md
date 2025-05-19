# 🌡️ Real-Time Temperature Monitoring with RabbitMQ, PostgreSQL & FastAPI

Simulate and stream temperature sensor data using a real-time pipeline powered by **RabbitMQ**, **PostgreSQL**, and **FastAPI**. This project publishes synthetic temperature data, processes it via RabbitMQ, stores it in a PostgreSQL database, and broadcasts updates to WebSocket-connected clients.

---

## 📦 Tech Stack

* 🐍 **Python**
* 🐇 **RabbitMQ** – message broker for decoupled communication
* 🐘 **PostgreSQL** – relational database for persistent storage
* ⚡ **FastAPI** – web framework with WebSocket support
* 📬 **Pika** – RabbitMQ client library for Python
* 🛢️ **psycopg2** – PostgreSQL adapter for Python

---

## 📁 Project Structure

```
realtime-temp-monitor/
├── producer.py       # Sends temperature data to RabbitMQ
├── consumer.py        # Listens to RabbitMQ and stores data in PostgreSQL
├── main.py/             # FastAPI app with WebSocket endpoint
├── db_setup.py/              # DB setup and schema scripts
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Install Requirements

Ensure **RabbitMQ** and **PostgreSQL** are running locally.

```bash
# Clone the repository
git clone https://github.com/your-username/realtime-temp-monitor.git
cd temperature-streaming

# Install Python dependencies
pip install -r requirements.txt
```

### 2️⃣ Set Up the Database

```bash
python db/db_setup.py
```

### 3️⃣ Start the Temperature Producer

```bash
python producer/producer.py
```

### 4️⃣ Start the WebSocket API Server

```bash
uvicorn app.main:app --reload
```

---

## 🔌 WebSocket Endpoint

Connect your WebSocket client (Postman, browser, frontend) to:

```
ws://localhost:8000/ws/temperature
```

All connected clients will receive live temperature updates in real-time.

---

## 📊 Sample Use Case

* IoT simulation for temperature monitoring
* Real-time dashboards for sensor networks
* Prototyping pub/sub and streaming pipelines

---

## 🧠 Future Enhancements

* Store timestamps with each reading
* Add Grafana or Streamlit dashboard
* Deploy using Docker or Kubernetes
* Add authentication for WebSocket connections

---
![image](https://github.com/user-attachments/assets/80a6f77c-7ccb-4b4a-9cd5-9d8af358104e)
---
## 💭 Output
  The output is stored in Postgres 
```
["id","value","timestamp"
1,32.53,"2025-05-19 11:05:06.824135"
2,27.53,"2025-05-19 11:05:08.822743"
3,39.08,"2025-05-19 11:05:10.852203"
4,35.82,"2025-05-19 11:05:12.835395"
5,38.22,"2025-05-19 11:05:14.830645"]
```
