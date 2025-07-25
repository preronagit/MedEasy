from googletrans import Translator

def translate_text(text, lang_code):
    translator = Translator()
    return translator.translate(text, dest=lang_code).text
