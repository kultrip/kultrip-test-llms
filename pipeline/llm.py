def generate_llm_suggestions(destination, preferences):
    # Simulate LLM-generated activities based on destination & preferences
    return [
        {
            "activity_id": "LLM001",
            "location": "Le Marais",
            "activity": "Historic Café Tour",
            "description": "Sip coffee in Parisian cafés with rich history and local stories.",
            "source": "llm",
            "available_through_agency": False,
            "preferences": ["food", "history"],
            "suitable_for": ["solo", "couple"],
            "seasonality": ["spring", "summer", "fall"],
            "price": 12.0,
            "booking_url": "",
            "rating": 4.2,
            "image_url": "",
            "category": "food"
        },
        {
            "activity_id": "LLM002",
            "location": "Jardin du Luxembourg",
            "activity": "Outdoor Yoga Session",
            "description": "Start your day with a relaxing yoga class in the gardens.",
            "source": "llm",
            "available_through_agency": False,
            "preferences": ["wellness", "outdoors"],
            "suitable_for": ["solo", "couple", "family"],
            "seasonality": ["spring", "summer"],
            "price": 8.0,
            "booking_url": "",
            "rating": 4.0,
            "image_url": "",
            "category": "wellness"
        },
        {
            "activity_id": "LLM003",
            "location": "Latin Quarter",
            "activity": "Bookshop Exploration",
            "description": "Wander through iconic bookshops and discover literary treasures.",
            "source": "llm",
            "available_through_agency": False,
            "preferences": ["arts", "literature", "walking"],
            "suitable_for": ["solo", "couple"],
            "seasonality": ["spring", "summer", "fall"],
            "price": 0.0,
            "booking_url": "",
            "rating": 4.3,
            "image_url": "",
            "category": "walking_tour"
        }
        # Add more LLM suggestions as needed
    ]