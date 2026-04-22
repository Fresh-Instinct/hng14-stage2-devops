### File: api/main.py
Line: 23
Issue: Redis connection used hardcoded localhost which fails in Docker
Fix: Replaced with environment variable REDIS_HOST

### File: api/main.py
**Line: 17**  
**Issue:** Redis `status.decode()` error on string  
**Fix:** `decode_responses=True` + removed `.decode()`

### File: api/main.py
**Line: 23-30**  
**Issue:** broken path  
**Fix:** `os.path.join(os.path.dirname(__file__), "../frontend/views/index

### File: api/main.py
**Line: 35-42**  
**Issue:** Missing `POST /jobs` endpoint causing 405 errors  
**Fix:** Added `@app.post("/jobs")` endpoint to handle job creation

### File: api/main.py
**Line: 43**  
**Issue:** Incorrect use of `await` on non-async function (`return await get_status()`)  
**Fix:** Removed `await` and used direct Redis call (`r.hget()`)

### File: api/main.py
**Line: 44-50**  
**Issue:** Missing `GET /jobs/{id}` endpoint expected by frontend  
**Fix:** Added `@app.get("/jobs/{job_id}")` endpoint to fetch job status

### File: frontend/index.html
**Line: 85**  
**Issue:** Form calls undefined `handleSubmit` function  
**Fix:** Implemented `async function handleSubmit(event)` in frontend script
