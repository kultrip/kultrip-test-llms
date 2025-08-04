# API Request & Response Examples

## Itinerary Generation Endpoint

**POST** `/generate_itinerary`

### Request Example

```json
{
  "destination": "Rome",
  "story": "A culinary adventure through ancient streets",
  "preferences": ["gastronomy", "arts", "history"],
  "duration": 4,
  "date_of_trip": "2025-09-15",
  "number_of_travelers": 2,
  "traveler_style": "couple"
}
```

### Parameters Explained

- `destination`: City or region for the trip.
- `story`: The inspiration or theme for the trip.
- `preferences`: List of traveler interests (e.g., sports, museums, gastronomy).
- `duration`: Number of days for the itinerary.
- `date_of_trip`: Starting date of the trip (YYYY-MM-DD).
- `number_of_travelers`: Integer count of travelers.
- `traveler_style`: Type of travelers (`"solo"`, `"couple"`, `"family"`, `"business"`).

### Response Example

```json
[
  {
    "day": 1,
    "location": "Trastevere",
    "activity": "Cooking Class",
    "description": "Master Roman recipes with a local chef.",
    "source": "getyourguide",
    "available_through_agency": true,
    "preferences": ["gastronomy"],
    "suitable_for": ["couple"],
    "seasonality": ["autumn", "spring"],
    "booking_url": "https://agency.example.com/book/rome-cooking"
  },
  {
    "day": 2,
    "location": "Vatican Museums",
    "activity": "Guided Art Tour",
    "description": "Explore Renaissance masterpieces.",
    "source": "tripadvisor",
    "available_through_agency": false,
    "preferences": ["arts", "history"],
    "suitable_for": ["family", "couple"],
    "seasonality": ["all"],
    "booking_url": null
  }
]
```

---