from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200

def test_submit_job():
    r = client.post("/submit")
    assert "job_id" in r.json()

def test_jobs_endpoint():
    r = client.get("/jobs")
    assert r.status_code == 200
