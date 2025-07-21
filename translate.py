import frappe
import requests

@frappe.whitelist()
def translate_to_arabic(text):
    try:
        response = requests.post("https://libretranslate.de/translate", data={{
            "q": text,
            "source": "en",
            "target": "ar",
            "format": "text"
        }})

        if response.status_code == 200:
            return response.json().get("translatedText")
        else:
            frappe.throw("Translation API error")

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Translation Error")
        frappe.throw("Translation failed due to server error")
