import requests

API_URL = "https://mineru.net/api/parse"   # example endpoint

def parse_pdf(file_path):

    with open(file_path, "rb") as f:
        files = {"file": f}

        response = requests.post(API_URL, files=files)

    return response.json()