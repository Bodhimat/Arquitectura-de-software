from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    logging.info("Service1 root endpoint accessed")
    return {"message": "Hello from Service 1"}

@app.get("/health")
def health_check():
    logging.info("Service1 health check")
    return {"status": "healthy"}
