from google import genai
import json
import os

def processInput(): 
    client = genai.Client(api_key="AIzaSyCFW9utIVQo1bqfETG2s7TFEkEU0qLW93I")
    folder_path = "D:\GOOGLE-AI\PRJECT\Input"
    output_folder = "D:\GOOGLE-AI\PRJECT\database"

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".jpg") or file_name.lower().endswith(".jpeg"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "rb") as img_file:
                image_data = img_file.read()
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                {
                    "parts": [
                        {"text": "Descrie ce vezi în această imagine și returnează informațiile într-un obiect JSON valid care sa contina doar un array numit items in care sa se afle fiecare nume de produs cu cantitatea si pretul lui. Nu adăuga alt text."},
                        {"inline_data": {"mime_type": "image/jpeg", "data": image_data}}
                    ]
                }
            ]
        )
        json_obj = json.loads(response.json())
        text_value = json_obj["candidates"][0]["content"]["parts"][0]["text"]
        text_value = text_value[8:-3]
        hopefully_works = json.loads(text_value)
        output_file = os.path.join(output_folder, f"processed_{file_name}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(hopefully_works, f, ensure_ascii=False, indent=4)

