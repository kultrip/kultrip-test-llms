def build_itinerary(data, duration=3):
    # Return first N activities as itinerary
    return {"itinerary": data[:duration]}