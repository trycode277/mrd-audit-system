from fastapi import FastAPI
from routes.upload import router as upload_router

app = FastAPI(title="MRD Compliance Audit API")

app.include_router(upload_router)

@app.get("/")
def home():
    return {"message": "MRD Audit System Running"}