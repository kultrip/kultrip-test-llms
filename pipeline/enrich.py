def enrich(data):
    for activity in data:
        activity["enriched"] = True
    return data