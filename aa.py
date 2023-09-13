import spacy
import streamlit as st

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Streamlit app title and description
st.title("Text Cleaning with spaCy")
st.write("Enter a text paragraph, and we'll remove stop words for you!")

# User input for the text paragraph
text = st.text_area("Enter your text here:")

if text:
    # Process the text with spaCy
    doc = nlp(text)

    # Initialize a list to store important keywords (non-stop words)
    keywords = []

    # Iterate through the tokens and keep non-stop words
    for token in doc:
        if not token.is_stop:
            keywords.append(token.text)

    # Join the non-stop words to form a cleaned paragraph
    cleaned_text = ' '.join(keywords)

    # Display the original and cleaned text
    st.subheader("Original Text:")
    st.write(text)
    st.subheader("Cleaned Text (Without Stop Words):")
    st.write(cleaned_text)
