import spacy

def load_spacy_model(model_name="en_core_web_sm"):
    """Load SpaCy model with error handling."""
    try:
        nlp = spacy.load(model_name)
        return nlp
    except OSError:
        raise RuntimeError(
            f"Error: SpaCy model '{model_name}' not found.\n"
            f"Run: python -m spacy download {model_name}"
        )
    except Exception as e:
        raise RuntimeError(f"Unexpected error loading SpaCy model: {e}")

# Load model safely
nlp = load_spacy_model()

import re

def parse_resume(text: str) -> dict:
    """Parse resume text using SpaCy NLP."""
    doc = nlp(text)

    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    organizations = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]

    degree_keywords = [
        "bachelor", "master", "mba", "b.e.", "b.tech", "m.e.", "m.tech", "phd", "doctorate",
        "degree", "engineering", "computer science", "information technology", "science", "arts"
    ]
    education_lines = [line.strip() for line in text.splitlines() if line.strip()]

    degrees = []
    institutions = []
    for line in education_lines:
        low = line.lower()
        if any(keyword in low for keyword in degree_keywords):
            if line not in degrees:
                degrees.append(line)

        if any(word in low for word in ["university", "college", "institute", "academy", "school"]):
            if line not in institutions:
                institutions.append(line)

    # add organizations from NER as possible institutions if not already included
    for org in organizations:
        if org not in institutions:
            institutions.append(org)

    parsed_data = {
        "Names": names,
        "Organizations": organizations,
        "Dates": dates,
        "Degrees": degrees,
        "Institutions": institutions,
    }
    return parsed_data
