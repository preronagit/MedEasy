import openai

def get_medicine_suggestion(symptoms, api_key):
    openai.api_key = api_key
    prompt = f"A patient reports the following symptoms or prescription: {symptoms}. Suggest medicines with dosage."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
