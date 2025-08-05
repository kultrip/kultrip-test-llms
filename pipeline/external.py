def fetch_external_activities(destination, preferences):
    # Mock data for GetYourGuide and Viator activities
    return [
        {
            "activity_id": "GYG001",
            "location": "Musée d'Orsay",
            "activity": "Impressionist Masterpieces Tour",
            "description": "Guided tour of Impressionist masterpieces at Musée d'Orsay.",
            "source": "getyourguide",
            "available_through_agency": True,
            "preferences": ["arts", "museum"],
            "story_tags": ["impressionism", "monet", "renoir"],  # ADDED
            "suitable_for": ["couple", "solo"],
            "seasonality": ["spring", "summer"],
            "price": 22.0,
            "booking_url": "https://agency.example.com/booking/orsay",
            "rating": 4.5,
            "image_url": "https://getyourguide.com/images/orsay.jpg",
            "category": "museum"
        },
        {
            "activity_id": "VT001",
            "location": "Versailles",
            "activity": "Versailles Palace Day Trip",
            "description": "Full-day trip to the Palace of Versailles with priority access.",
            "source": "viator",
            "available_through_agency": True,
            "preferences": ["history", "sightseeing"],
            "story_tags": ["versailles", "louis xiv"],  # ADDED
            "suitable_for": ["family", "couple"],
            "seasonality": ["spring", "summer", "fall"],
            "price": 65.0,
            "booking_url": "https://agency.example.com/booking/versailles",
            "rating": 4.8,
            "image_url": "https://viator.com/images/versailles.jpg",
            "category": "landmark"
        },
        {
            "activity_id": "GYG002",
            "location": "Notre Dame",
            "activity": "Cathedral Walking Tour",
            "description": "Explore Notre Dame and the surrounding area with a local guide.",
            "source": "getyourguide",
            "available_through_agency": True,
            "preferences": ["history", "walking"],
            "story_tags": ["hugo", "notre dame", "les misérables"], # ADDED
            "suitable_for": ["solo", "couple", "family"],
            "seasonality": ["spring", "summer", "fall"],
            "price": 18.0,
            "booking_url": "https://agency.example.com/booking/notredame",
            "rating": 4.3,
            "image_url": "https://getyourguide.com/images/notredame.jpg",
            "category": "walking_tour"
        },
        {
            "activity_id": "VT002",
            "location": "Montparnasse Tower",
            "activity": "Observation Deck Experience",
            "description": "See panoramic views of Paris from Montparnasse Tower.",
            "source": "viator",
            "available_through_agency": True,
            "preferences": ["sightseeing"],
            "story_tags": [],  # No story match
            "suitable_for": ["solo", "couple", "family"],
            "seasonality": ["spring", "summer", "fall", "winter"],
            "price": 20.0,
            "booking_url": "https://agency.example.com/booking/montparnasse",
            "rating": 4.4,
            "image_url": "https://viator.com/images/montparnasse.jpg",
            "category": "landmark"
        },
        # Add more mock activities here as needed
    ]