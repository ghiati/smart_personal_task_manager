import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def parse_command(command):
    doc = nlp(command)
    tasks = []
    for ent in doc.ents:
        if ent.label_ == "TIME":
            tasks.append(f"Time: {ent.text}")
        elif ent.label_ == "DATE":
            tasks.append(f"Date: {ent.text}")
    # You can expand this function to handle more sophisticated parsing
    return tasks
