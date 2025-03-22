from google import genai
import json

client = genai.Client(api_key="AIzaSyCFW9utIVQo1bqfETG2s7TFEkEU0qLW93I")
image_path = "D:\GOOGLE-AI\PRJECT\ex.jpeg"
with open(image_path, "rb") as img_file:
    image_data = img_file.read()

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        {
            "parts": [
                {"text": "Descrie ce vezi în această imagine și returnează informațiile într-un obiect JSON valid. Nu adăuga alt text."},
                {"inline_data": {"mime_type": "image/jpeg", "data": image_data}}
            ]
        }
    ]
)
print(response.json())
print(type(response.json()))
json_obj = json.loads(response.json())
print(json_obj)

text_value = json_obj["candidates"][0]["content"]["parts"][0]["text"]

text_value = text_value[8:-3]
hopefully_works = json.loads(text_value)
output_file = "output2.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(hopefully_works, f, ensure_ascii=False, indent=4)
