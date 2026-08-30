def total_sales(data: list):
    sum = 0

    for line in data:
        sum += line["price"] * line["quantity"]

    print(f"Total revenue: {sum}€")

def sales_by_category(data: list):
    categories = aggregate_projection(data, "value", "category")

    print("Revenue by categories:")
    for category in categories:
        print(f"{category["category"]}: {category["value"]}€")

def top_customer(data: list):
    customers = aggregate_projection(data, "value", "customer")

    top_spent = 0
    top_name = ""
    for customer in customers:
        if customer["value"] > top_spent:
            top_spent = customer["value"]
            top_name = customer["customer"]

    print(f"Top customer: {top_name} - {top_spent}€")

def top_product(data: list):
    products = aggregate_projection(data, "quantity", "product")

    top_quantity = 0
    top_name = ""
    for product in products:
        if product["quantity"] > top_quantity:
            top_quantity = product["quantity"]
            top_name = product["product"]

    print(f"Top Product: {top_name} - {top_quantity} sold")



def aggregate_projection(data: list, aggregate_attribute, projection_key: str):
    attributes = []

    for line in data:
        if (contains_attribute(attributes, projection_key, line[projection_key])):
            for attribute in attributes:
                if (attribute[projection_key] == line[projection_key]):
                    attribute[aggregate_attribute] += (line[aggregate_attribute])
        else:
            record = {
                projection_key: line[projection_key],
                aggregate_attribute: line[aggregate_attribute]
            }
            attributes.append(record)

    return attributes

def contains_attribute(data: list, attribute: str, value):
    for line in data:
        if(line[attribute] == value): return True
    return False