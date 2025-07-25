import requests
import streamlit as st

def get_medicine_suggestion(prompt):
    api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    hf_api_key = st.secrets["hf_api_key"]
    
    headers = {
        "Authorization": f"Bearer {hf_api_key}"
    }
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True}
    }

    response = requests.post(api_url, headers=headers, json=payload)
    
    try:
        return response.json()[0]["generated_text"]
    except Exception as e:
        return "Sorry, failed to get a suggestion. Please try again."
