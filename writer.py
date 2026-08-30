import json

def write_data(data: list, filename: str):
    with open(filename, "w") as f:
        json.dump(data, f, indent = 4)