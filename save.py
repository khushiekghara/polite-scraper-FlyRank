import json
import os


def save_json(data):
    os.makedirs("data", exist_ok=True)

    with open("data/products.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("Data saved successfully to data/products.json")