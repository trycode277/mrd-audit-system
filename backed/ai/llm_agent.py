import ollama

def analyze_medical_record(text):

    prompt = f"""
You are a medical record audit AI.

Extract these fields:

patient_name
age
diagnosis
doctor

Then calculate:

compliance_score (0-100)
missing_fields
risk_level (High Risk if score < 60 else Low Risk)

Return ONLY JSON.

Medical Record:
{text}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]