# collector.py
# FastAPI collector for receiving IDS alerts and saving them to Postgres

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv  # Load .env

# Load environment variables from .env
load_dotenv()

app = FastAPI()

DB_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("COLLECTOR_API_KEY")

# Debug prints
print("DEBUG: DATABASE_URL =", DB_URL)
print("DEBUG: COLLECTOR_API_KEY =", API_KEY)

class Alert(BaseModel):
    src_ip: str
    ports: list[int]
    timestamp: int
    sensor_id: str

@app.post("/api/alerts")
def receive_alert(alert: Alert, authorization: str = Header(default="")):
    print("DEBUG: Received Authorization header:", authorization)

    if authorization != f"Bearer {API_KEY}":
        print("DEBUG: Unauthorized access attempt")
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO alerts (src_ip, ports, timestamp, sensor_id) VALUES (%s, %s, %s, %s)",
            (alert.src_ip, alert.ports, alert.timestamp, alert.sensor_id)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("DEBUG: Database error:", e)
        return {"status": "error", "message": str(e)}

    return {"status": "success"}
