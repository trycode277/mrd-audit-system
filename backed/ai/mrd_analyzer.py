import json

def analyze_mrd(text):

    text = text.lower()

    checklist = [
        "admission slip",
        "admission order",
        "mlc copy",
        "discharge summary",
        "dama summary",
        "death summary",
        "case record",
        "case sheet",
        "consultation sheet",
        "progress sheet",
        "high risk consent",
        "procedure consent",
        "surgery consent form",
        "pre operative checklist",
        "consent for hiv",
        "anesthesia record",
        "anesthesia consent",
        "pac",
        "operation notes",
        "surgery report",
        "tpr chart",
        "nurses notes",
        "doctor treatment chart",
        "intake output chart",
        "monitoring chart",
        "ventilator chart",
        "investigation report",
        "dama consent form",
        "blood transfusion consent",
        "ip billing sheet",
        "patient information sheet",
        "opd sheet",
        "birth details",
        "er observation chart",
        "dialysis flow sheet"
    ]

    results = []

    for item in checklist:

        if item in text:
            comment = "Present"
        else:
            comment = "Missing"

        results.append({
            "page_number": 1,
            "checklist_name": item,
            "comment": comment
        })

    return {"mrd_audit": results}