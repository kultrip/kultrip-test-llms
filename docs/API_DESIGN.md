# API Design

## **Endpoint: `/generate_itinerary` (POST)**

### **Request Body**

```json
{
  "destination": "Wonderland",
  "story": "Alice wanders through magical lands",
  "preferences": ["arts", "gastronomy"],
  "duration": 5,
  "date_of_trip": "2025-08-10",
  "number_of_travelers": 2,
  "traveler_style": "couple"
}
```

### **Response**

```json
[
  {
    "day": 1,
    "location": "Wonderland Gardens",
    "activity": "Photography",
    "description": "Capture magical moments...",
    "source": "agency",
    "available_through_agency": true,
    "preferences": ["arts"],
    "suitable_for": ["couple"],
    "seasonality": ["summer"],
    "price": 40.0,
    "booking_url": "https://agency.example.com/booking/123"
  },
  ...
]
```

## **Other Endpoints (Future)**
- `/activities` (GET): List/filter available activities.
- `/sources` (GET): Get list of sources and their status.