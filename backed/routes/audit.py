from fastapi import APIRouter, UploadFile, File
import shutil
import os

from ai.mineru_parser import parse_pdf_with_mineru

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_record(file: UploadFile = File(...)):

    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # run MinerU parsing
    parsed_data = parse_pdf_with_mineru(path)

    return {
        "filename": file.filename,
        "mineru_output": parsed_data
    }