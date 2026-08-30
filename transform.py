def transform_data(data: list):
    total = len(data)
    removed = 0

    for i in range(total):
        i_corrected = i - removed

        try:
            try_parse(data[i_corrected])
        except ValueError:
            print(f"Error in line {i + 1}: parsing failed!")
            data.remove(data[i_corrected])
            removed += 1

        data[i_corrected]["value"] = data[i_corrected]["price"] * data[i_corrected]["quantity"]

    print(f"{len(data)} / {total} lines loaded!")

    return data

def try_parse(line):
    line["id"] = int(line["id"])
    line["price"] = float(line["price"])
    line["quantity"] = int(line["quantity"])