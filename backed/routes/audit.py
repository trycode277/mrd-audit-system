from fastapi import APIRouter, UploadFile, File
import shutil
import os

from ai.ocr_engine import extract_text
from ai.mrd_analyzer import analyze_mrd

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_record(file: UploadFile = File(...)):

    try:

        path = os.path.join(UPLOAD_DIR, file.filename)

        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {
            "filename": file.filename,
            "compliance_score": 80,
            "risk_level": "Low Risk Record",
            "structured_data": {
                "patient_name": "Demo Patient",
                "age": "45",
                "diagnosis": "Fever",
                "doctor": "Dr Sharma"
            },
            "missing_fields": ["discharge_summary"]
        }

    except Exception as e:

        return {"error": str(e)}