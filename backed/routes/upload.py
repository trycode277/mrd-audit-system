from fastapi import APIRouter, UploadFile, File
import shutil
from ai.ocr_engine import extract_text
from ai.mrd_analyzer import analyze_mrd

router = APIRouter()

@router.post("/upload")
async def upload_record(file: UploadFile = File(...)):

    filepath = f"uploads/{file.filename}"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(filepath)

    audit_result = analyze_mrd(text)

    return audit_result