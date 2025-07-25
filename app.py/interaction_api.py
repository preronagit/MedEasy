import requests

def check_interactions(drug_name):
    try:
        url = f"https://api.fda.gov/drug/label.json?search=drug_interactions:{drug_name}"
        response = requests.get(url)
        data = response.json()
        return data["results"][0].get("drug_interactions", "No data found.")
    except:
        return "No interaction data available."
