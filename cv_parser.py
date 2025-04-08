import docx
from pdfminer.high_level import extract_text
import spacy

nlp = spacy.load("en_core_web_sm")

def parse_cv(file_path):
    # Read PDF, DOCX, or TXT
    if file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    elif file_path.endswith('.pdf'):
        text = extract_text(file_path)
    else:
        with open(file_path, 'r') as f:
            text = f.read()
    
    return analyze_text(text)

def analyze_text(text):
    doc = nlp(text)
    
    # Extract skills (nouns) and experiences (companies)
    skills = []
    experiences = []
    
    for ent in doc.ents:
        if ent.label_ == "ORG":  # Organizations (companies)
            experiences.append(ent.text)
    
    for token in doc:
        if token.pos_ == "NOUN" and len(token.text) > 3:  # Simple skill detection
            skills.append(token.text)
    
    return {
        'skills': list(set(skills)),  # Remove duplicates
        'experiences': list(set(experiences)),
        'raw_text': text
    }