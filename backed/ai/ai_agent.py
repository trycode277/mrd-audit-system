import re

def analyze_record(text):

    text = text.lower()

    data = {
        "patient_name": None,
        "age": None,
        "diagnosis": None,
        "doctor": None
    }

    name = re.search(r'patient name[:\- ]+(.*)', text)
    age = re.search(r'age[:\- ]+(\d+)', text)
    diagnosis = re.search(r'diagnosis[:\- ]+(.*)', text)
    doctor = re.search(r'doctor[:\- ]+(.*)', text)

    if name:
        data["patient_name"] = name.group(1)

    if age:
        data["age"] = age.group(1)

    if diagnosis:
        data["diagnosis"] = diagnosis.group(1)

    if doctor:
        data["doctor"] = doctor.group(1)

    return data


def compliance_score(data):

    total = len(data)

    present = sum(1 for v in data.values() if v)

    score = int((present / total) * 100)

    missing = [k for k, v in data.items() if not v]

    if score < 60:
        risk = "High Risk Record"
    else:
        risk = "Low Risk Record"

    return score, missing, risk