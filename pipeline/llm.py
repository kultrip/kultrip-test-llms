def generate_llm_suggestions(destination, preferences):
    # Later: Call OpenAI, Anthropic, etc. with context and prompt!
    # For now, mock suggestions
    return [
        {
            "location": "Luxembourg Gardens",
            "activity": "Poetry Reading",
            "description": "Join a local poetry group for an afternoon reading.",
            "source": "llm",
            "available_through_agency": False,
            "preferences": ["arts", "literature"],
            "suitable_for": ["solo", "couple"],
            "seasonality": ["spring", "summer"],
            "price": 0.0,
            "booking_url": ""
        }
    ]