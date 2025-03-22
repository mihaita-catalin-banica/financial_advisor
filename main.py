from flask import Flask, render_template, jsonify
import json
import os
from file1 import processInput
from file2 import createTable

processInput()
createTable()

app = Flask(__name__)

data_folder = "D:\GOOGLE-AI\PRJECT\database"  # Modifică dacă e necesar

def load_data():
    items = []
    total = {"total_spent": 0, "percentage": "100.00%"}

    for file_name in os.listdir(data_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(data_folder, file_name)
            with open(file_path, "r", encoding="utf-8") as json_file:
                try:
                    data = json.load(json_file)
                    if 'items' in data and isinstance(data['items'], list):
                        items.extend(data['items'])
                except json.JSONDecodeError:
                    print(f"Error loading {file_name}")

    if items:
        for item in items:
            item["quantity"] = item.get("quantity", 1)
            item["price"] = item.get("price", 0)
            item["amount"] = item.get("Total Spent (Lei)", item["quantity"] * item["price"])  
        
        total["total_spent"] = sum(float(item["amount"]) for item in items)
        for item in items:
            item["percentage"] = f"{(float(item['amount']) / total['total_spent']) * 100:.2f}%" if total["total_spent"] > 0 else "0.00%"

    return items, total


@app.route('/')
def index():
    items, total = load_data()
    return render_template('index.html', items=items, total=total)

if __name__ == '__main__':
    app.run(debug=True)