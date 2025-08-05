def fetch_kultrip_activities(destination, preferences):
    # Replace with internal activity lookup!
    return [
        {
            "activity_id": "KT001",
            "location": "Montmartre",
            "activity": "Art Walk",
            "description": "Discover Parisian street art and local galleries.",
            "source": "kultrip",
            "available_through_agency": False,
            "preferences": ["arts", "walking"],
            "suitable_for": ["solo", "couple"],
            "seasonality": ["spring", "summer", "fall"],
            "price": 0.0,
            "booking_url": "",
            "rating": 4.6,
            "image_url": "https://kultrip.com/images/montmartre.jpg",
            "category": "walking_tour"
        },
        {
            "activity_id": "KT002",
            "location": "Seine River",
            "activity": "Evening Picnic",
            "description": "Enjoy a relaxing picnic by the river.",
            "source": "kultrip",
            "available_through_agency": False,
            "preferences": ["gastronomy", "outdoors"],
            "suitable_for": ["couple", "family"],
            "seasonality": ["summer"],
            "price": 15.0,
            "booking_url": "",
            "rating": 4.4,
            "image_url": "https://kultrip.com/images/seine-picnic.jpg",
            "category": "picnic"
        },
        {
            "activity_id": "KT003",
            "location": "Le Marais",
            "activity": "Vintage Shopping",
            "description": "Explore quirky vintage shops in the historic Marais district.",
            "source": "kultrip",
            "available_through_agency": False,
            "preferences": ["shopping", "walking"],
            "suitable_for": ["solo", "couple", "family"],
            "seasonality": ["spring", "summer", "fall"],
            "price": 0.0,
            "booking_url": "",
            "rating": 4.7,
            "image_url": "https://kultrip.com/images/marais-vintage.jpg",
            "category": "shopping"
        }
        # Add more curated activities as needed
    ]