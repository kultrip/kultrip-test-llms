# Data Model for Activities

Each activity from any source should follow this structure:

```python
{
    "story": "Alice wanders through magical lands",
    "location": "Wonderland Gardens",
    "activities": ["Photography", "Picnic"],
    "description": "Capture magical moments and enjoy a picnic at Wonderland Gardens.",
    "preferences": ["arts", "outdoors", "family"],
    "available_through_agency": True,
    "suitable_for": ["family", "solo", "couple"],
    "seasonality": ["spring", "summer"],
    "source": "agency",  # or kultrip, tripadvisor, etc.
    "price": 40.0,
    "booking_url": "https://agency.example.com/booking/123"
}
```

## Fields Explained

- **story**: The inspiration or theme for the activity.
- **location**: Where it takes place.
- **activities**: List of actions (e.g. ["Museum Visit", "Cooking Class"]).
- **description**: Short blurb.
- **preferences**: Interests the activity matches ("sports", "gastronomy", etc).
- **available_through_agency**: If bookable via agency.
- **suitable_for**: Traveler types ("solo", "family", etc).
- **seasonality**: Relevant seasons or months.
- **source**: Where the activity was sourced.
- **price**: (optional) Estimated price.
- **booking_url**: (optional) Direct booking link.

## How to Use

- Update existing data sources to conform to this format.
- When adding new sources, map their data into this structure.