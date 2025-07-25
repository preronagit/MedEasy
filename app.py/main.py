import streamlit as st
from ocr_api import extract_text_ocr_space
from med_api import get_medicine_suggestion  
from interaction_api import check_interactions
from utils import translate_text

# Set up Streamlit page
st.set_page_config(page_title="MedEasy", page_icon="💊")
st.title("💊 MedEasy - AI Pharmacist Assistant")

# Load secrets from .streamlit/secrets.toml
ocr_api_key = st.secrets["ocr_space_api_key"]
hf_api_key = st.secrets["hf_api_key"] 

# File uploader for prescription
uploaded_file = st.file_uploader("Upload your prescription image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.info("Extracting text from image...")
    extracted_text = extract_text_ocr_space(uploaded_file, api_key=ocr_api_key)
    st.success("Extracted Text:")
    st.text_area("Prescription Text", value=extracted_text, height=150)

    if extracted_text:
        st.subheader("💊 Suggested Medicines")
        suggestion = get_medicine_suggestion(extracted_text)
        st.write(suggestion)

        st.subheader("⚠️ Drug Interaction Check")
        drug_name = st.text_input("Enter a drug name to check interactions", "paracetamol")
        if drug_name:
            interactions = check_interactions(drug_name)
            st.info(interactions)

        st.subheader("🌐 Translate")
        lang = st.selectbox("Choose language", ["en", "hi", "bn", "ta", "te"])
        translated = translate_text(suggestion, lang)
        st.write(f"**Translated Text ({lang})**: {translated}")
