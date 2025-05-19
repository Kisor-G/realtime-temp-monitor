import psycopg2

def setup_db():
    conn = psycopg2.connect(
        dbname='postgres',  
        user='postgres',
        password='your_password',
        host='localhost'
    )
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_database WHERE datname='sensor_db'")
    if not cur.fetchone():
        cur.execute("CREATE DATABASE sensor_db")
        print("✅ Created database 'sensor_db'")
    else:
        print("ℹ️ Database 'sensor_db' already exists")

    cur.close()
    conn.close()

    conn = psycopg2.connect(
        dbname='sensor_db',
        user='postgres',
        password='your_password',
        host='localhost'
    )
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS temperature_data (
        id SERIAL PRIMARY KEY,
        value FLOAT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Table 'temperature_data' ready")

if __name__ == "__main__":
    setup_db()
