# 🚀 DevOps Stage 2 – Microservices Application

This project is a containerized microservices application consisting of:

* **Frontend (Node.js)** – user interface for submitting and tracking jobs
* **API (FastAPI)** – handles job creation and status retrieval
* **Worker (Python)** – processes jobs asynchronously
* **Redis** – message broker / queue

---

# Prerequisites

Ensure the following are installed on your machine:

* **Git**
* **Docker**
* **Docker Compose (v2+)**

---

# 1. Clone the Repository

```bash
git clone https://github.com/Fresh-Instinct/hng14-stage2-devops.git
cd hng14-stage2-devops
```

---

# 2. Configure Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` if needed:

```env
REDIS_HOST=redis
REDIS_PORT=6379
API_HOST=api
API_PORT=8000
FRONTEND_PORT=3000
```

---

# 3. Build and Start the Application

Run:

```bash
docker compose up --build
```

This will:

* Build Docker images for all services
* Start containers for:

  * frontend
  * api
  * worker
  * redis
* Create an internal network for communication

---

# 4. Verify Services Are Running

Check running containers:

```bash
docker ps
```

Check logs:

```bash
docker compose logs -f
```

---

# 5. Access the Application

Open your browser:

```
http://localhost:3000
```

---

# 6. Test the System

## Submit a Job

```bash
curl -X POST http://localhost:8000/jobs \
  -H "Content-Type: application/json" \
  -d '{"task": "test"}'
```
-

# 7. Stop the Application

```bash
docker compose down
```

To remove volumes as well:

```bash
docker compose down -v
```

---

# 8. Troubleshooting

## Check logs per service

```bash
docker compose logs api
docker compose logs worker
docker compose logs frontend
docker compose logs redis
```


# 📌 9. Notes

* All services communicate via an internal Docker network
* Redis is not exposed externally
* Configuration is handled via environment variables
* Health checks are implemented for production readiness

---

# ✅ Expected Successful Startup

When everything is working:

* All containers show **Up** status
* No continuous errors in logs
* Frontend loads in browser
* Jobs can be submitted and processed successfully

---

# 📄 Additional Documentation

* `FIXES.md` → All bugs identified and resolved
* `.env.example` → Required environment variables

---

# 🎯 Summary

To run the entire system:

```bash
git clone <repo>
cd hng14-stage2-devops
cp .env.example .env
docker compose up --build
```

---

If the system starts and processes jobs successfully, your setup is complete ✅

