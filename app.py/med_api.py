import requests
import streamlit as st

def get_medicine_suggestion(prompt):
    api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    headers = {
        "Authorization": f"Bearer {st.secrets['hf_api_key']}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": f"Suggest medicines based on this prescription: {prompt}",
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
