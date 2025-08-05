def fetch_agency_activities(destination, preferences):
    # Replace with real API/db queries later!
    return [
        {
            "location": "Louvre Museum",
            "activity": "Museum Visit",
            "description": "Explore world-class art at the Louvre.",
            "source": "agency",
            "available_through_agency": True,
            "preferences": ["arts"],
            "suitable_for": ["couple", "solo"],
            "seasonality": ["spring", "summer"],
            "price": 25.0,
            "booking_url": "https://agency.example.com/booking/louvre"
        },
        {
            "location": "Eiffel Tower",
            "activity": "Guided Tower Tour",
            "description": "Enjoy panoramic views of Paris.",
            "source": "agency",
            "available_through_agency": True,
            "preferences": ["sightseeing"],
            "suitable_for": ["couple", "family"],
            "seasonality": ["spring", "summer", "fall"],
            "price": 30.0,
            "booking_url": "https://agency.example.com/booking/eiffel"
        },
    ]