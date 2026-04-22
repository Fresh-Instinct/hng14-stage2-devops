from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import redis
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

r = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        decode_responses=True
        )

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    html_path = os.path.join(os.path.dirname(__file__), "../frontend/views/index.html")
    with open(html_path, "r") as f:
        return f.read()

@app.post("/submit")
def create_job():
    job_id = str(uuid.uuid4())
    r.lpush("job", job_id)
    r.hset(f"job:{job_id}", "status", "queued")
    return {"job_id": job_id}

@app.get("/status/{job_id}")
def get_job_status(job_id: str):
    status = r.hget(f"job:{job_id}", "status")
    if not status:
        return {"error": "not found"}
    return {"job_id": job_id, "status": status}

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    status = r.hget(f"job:{job_id}", "status")
    return {"status": status or "not_found"}

@app.get("/jobs")
def list_jobs():
    return {"jobs": []}

@app.get("/health")
def health():
    return {"status": "ok"}
