def fetch_agency_activities(destination, preferences):
    # Expanded mock data for agency activities
    return [
        {
            "activity_id": "AG001",
            "location": "Louvre Museum",
            "activity": "Museum Visit",
            "description": "Explore world-class art at the Louvre.",
            "source": "agency",
            "available_through_agency": True,
            "preferences": ["arts"],
            "story_tags": ["da vinci", "renaissance"],  # ADDED
            "suitable_for": ["couple", "solo"],
            "seasonality": ["spring", "summer"],
            "price": 25.0,
            "booking_url": "https://agency.example.com/booking/louvre",
            "availability": "2025-08-10 to 2025-12-31",
            "rating": 4.8,
            "image_url": "https://agency.example.com/images/louvre.jpg",
            "category": "museum"
        },
        {
            "activity_id": "AG002",
            "location": "Eiffel Tower",
            "activity": "Guided Tower Tour",
            "description": "Enjoy panoramic views of Paris.",
            "source": "agency",
            "available_through_agency": True,
            "preferences": ["sightseeing"],
            "story_tags": ["midnight in paris"],  # ADDED
            "suitable_for": ["couple", "family"],
            "seasonality": ["spring", "summer", "fall"],
            "price": 30.0,
            "booking_url": "https://agency.example.com/booking/eiffel",
            "availability": "2025-08-01 to 2025-09-30",
            "rating": 4.7,
            "image_url": "https://agency.example.com/images/eiffel.jpg",
            "category": "landmark"
        },
        {
            "activity_id": "AG003",
            "location": "Seine River",
            "activity": "Evening River Cruise",
            "description": "Enjoy a romantic evening cruise along the Seine.",
            "source": "agency",
            "available_through_agency": True,
            "preferences": ["romance", "sightseeing"],
            "story_tags": ["romance", "midnight in paris"],  # ADDED
            "suitable_for": ["couple"],
            "seasonality": ["summer", "fall"],
            "price": 45.0,
            "booking_url": "https://agency.example.com/booking/seine-cruise",
            "availability": "2025-08-01 to 2025-10-15",
            "rating": 4.9,
            "image_url": "https://agency.example.com/images/seine.jpg",
            "category": "cruise"
        }
        # Add more activities as needed
    ]