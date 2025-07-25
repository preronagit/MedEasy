import requests

def extract_text_ocr_space(image_file, api_key):
    url = 'https://api.ocr.space/parse/image'
    payload = {'apikey': api_key}
    files = {'filename': image_file}
    response = requests.post(url, data=payload, files=files)
    result = response.json()
    return result['ParsedResults'][0]['ParsedText']
