import os
import json
from google import genai

def createTable():
    client = genai.Client(api_key="AIzaSyCFW9utIVQo1bqfETG2s7TFEkEU0qLW93I")

    json_folder = "D:/GOOGLE-AI/PRJECT/database"
    big_item_list = []

    for file_name in os.listdir(json_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(json_folder, file_name)
            with open(file_path, "r", encoding="utf-8") as json_file:
                try:
                    data = json.load(json_file)
                    if 'items' in data and isinstance(data['items'], list):
                        items = data['items']
                        big_item_list.append(items)
                    else:
                        print(f"File: {file_name} does not contain 'items' array.")
                
                except json.JSONDecodeError as e:
                    print(f"Error decoding {file_name}: {e}")

    big_item_list_json = json.dumps(big_item_list)

    content_string = (
        "Given the following item list, please calculate the total amount spent, "
        "as well as the amount spent on each individual item. For each item, "
        "calculate the percentage of the total spending it represents. "
        "Present the results clearly in a readable format, with each item showing "
        "the exact tabele head: item, quantity, price, total_spent, and its percentage of the total. "
        "Here is the item list: " + big_item_list_json
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=content_string
    )

    print(response.text)
