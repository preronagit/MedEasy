import requests
import streamlit as st

def get_medicine_suggestion(prompt):
    api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    headers = {
        "Authorization": f"Bearer {st.secrets['hf_api_key']}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": f"Suggest medicines based on this prescription: {prompdef get_medicine_suggestion(prescription_text):
    api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
    headers = {
        "Authorization": f"Bearer {st.secrets['hf_api_key']}",
        "Content-Type": "application/json"
    }

    prompt = f"""You are a medical assistant. Based on this prescription text, suggest possible medicines:

Prescription: {prescription_text}

Output:"""

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100},
        "options": {"wait_for_model": True}
    }

    response = requests.post(api_url, headers=headers, json=payload)

    try:
        json_response = response.json()
        if isinstance(json_response, list) and "generated_text" in json_response[0]:
            return json_response[0]["generated_text"].split("Output:")[-1].strip()
        else:
            return "⚠️ Unexpected model output format."
    except Exception as e:
        return f"❌ Error: {str(e)}"
t}",
        "options": {"wait_for_model": True}
    }

    response = requests.post(api_url, headers=headers, json=payload)

    try:
        response.raise_for_status()  # will raise an HTTPError if response code is not 200
        json_response = response.json()

        # Check format
        if isinstance(json_response, list) and "generated_text" in json_response[0]:
            return json_response[0]["generated_text"]
        else:
            return "⚠️ Unexpected model output format."
    except Exception as e:
        return f"❌ Error: {str(e)}"
