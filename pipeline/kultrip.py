def fetch_kultrip_activities(destination, preferences):
    # Replace with internal activity lookup!
    return [
        {
            "location": "Montmartre",
            "activity": "Art Walk",
            "description": "Discover Parisian street art and local galleries.",
            "source": "kultrip",
            "available_through_agency": False,
            "preferences": ["arts", "walking"],
            "suitable_for": ["solo", "couple"],
            "seasonality": ["spring", "summer", "fall"],
            "price": 0.0,
            "booking_url": ""
        },
        {
            "location": "Seine River",
            "activity": "Evening Picnic",
            "description": "Enjoy a relaxing picnic by the river.",
            "source": "kultrip",
            "available_through_agency": False,
            "preferences": ["gastronomy", "outdoors"],
            "suitable_for": ["couple", "family"],
            "seasonality": ["summer"],
            "price": 15.0,
            "booking_url": ""
        },
    ]