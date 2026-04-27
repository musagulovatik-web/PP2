import json
import os

def load_data(f, d):
    if not os.path.exists(f):
        return d
    with open(f, "r") as file:
        return json.load(file)

def save_data(f, data):
    with open(f, "w") as file:
        json.dump(data, file)