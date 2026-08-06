def clean_data(data):

    for item in data:

        item["price"] = item["price"].replace("£", "").strip()

    return data