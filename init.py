import json

def init():
    while True:
        path = input(f"Select file path for reading stored data (type 0 for no data): ")

        if path == "0":
            return []
        else:
            try:
                with open(path, "r") as f:
                    data = json.load(f)
            except:
                print("Invalid path!")
                continue
            else:
                return data