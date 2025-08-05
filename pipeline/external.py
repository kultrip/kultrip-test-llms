def fetch_external_activities(destination, preferences):
    # For now, mock data. Later: Call APIs or scrape!
    return [
        {
            "location": "Notre-Dame Cathedral",
            "activity": "Cathedral Tour",
            "description": "Guided tour of Notre-Dame's history and architecture.",
            "source": "tripadvisor",
            "available_through_agency": False,
            "preferences": ["history", "architecture"],
            "suitable_for": ["solo", "family"],
            "seasonality": ["spring", "summer", "fall"],
            "price": 20.0,
            "booking_url": "https://tripadvisor.com/booking/notredame"
        },
        {
            "location": "Paris Culinary School",
            "activity": "French Cooking Class",
            "description": "Learn to cook classic French dishes.",
            "source": "getyourguide",
            "available_through_agency": False,
            "preferences": ["gastronomy"],
            "suitable_for": ["couple", "family"],
            "seasonality": ["all"],
            "price": 50.0,
            "booking_url": "https://getyourguide.com/booking/paris-cooking"
        },
    ]