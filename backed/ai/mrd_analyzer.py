checklist = [
"admission slip",
"mlc copy",
"discharge summary",
"case sheet",
"consultation",
"consent",
"operation notes",
"tpr chart",
"nurse notes",
"treatment chart",
"intake output",
"monitoring chart",
"ventilator chart",
"investigation",
"billing",
"patient information"
]

def analyze_mrd(text):

    text = text.lower()

    result = {}

    for item in checklist:

        if item in text:
            result[item] = "Present"
        else:
            result[item] = "Missing"

    return result