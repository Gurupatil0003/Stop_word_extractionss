import streamlit as st
import spacy

# Load the spaCy NER model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Extract entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

# Streamlit UI
st.title("Entity Extraction App")

# Input text area for user to enter a paragraph
text = st.text_area("Enter a text paragraph:")

if st.button("Extract Entities"):
    # Ensure text is not empty
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Extract entities
        entities = extract_entities(text)
        
        # Display extracted entities
        if entities:
            st.header("Extracted Entities:")
            for entity, label in entities:
                st.write(f"- {entity} ({label})")
        else:
            st.info("No entities found in the text.")
