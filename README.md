# Credit Card Service

## RoadMap to UP
 + Clone repository
    + `$ git clone git@github.com:tachian/kanastra-service.git`

 + Create virtual env
   python3 -m venv <myenvname>

 + Install libs
   pip install -r requirements-dev.txt

 + Running tests
    pytest

 + Create image
    docker build -t kanastra .  

 + Run image to start API
    docker run -p 5000:5000 kanastra  

 + Run Scheduler - To send email/slips
    docker exec -it <CONTAINER ID> python scheduler.py

 + HEALTH endpoints
   + http://localhost:5000/api/health: If API is working, must show {"service": "API Kanastra HealthCheck", "version": "1.0"}

