import csv

def read_csv(filename: str):
    with open(filename) as f:
        lines = csv.DictReader(f)

        dicts = []
        for line in lines:
            dicts.append(line)

        return dicts