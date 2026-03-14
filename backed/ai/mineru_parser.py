import subprocess
import json
import os

def parse_pdf_with_mineru(pdf_path):

    # run MinerU parser
    subprocess.run([
        "magic-pdf",
        pdf_path
    ])

    # MinerU creates output json automatically
    json_file = pdf_path.replace(".pdf", ".json")

    if os.path.exists(json_file):

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data

    return {"error": "MinerU output not found"}