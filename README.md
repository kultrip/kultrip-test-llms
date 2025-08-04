# kultrip-test-llms

**Testing different LLMs for trip inspiration and itinerary building**

---

## Overview

This project aims to generate travel itineraries inspired by user stories, combining activities and experiences from multiple sources:

- **Agency**: Activities offered by travel agencies
- **Kultrip**: Proprietary or curated activities
- **LLMs**: Large Language Model-generated suggestions
- **Tripadvisor** (planned): Public activities, tours, and reviews
- **GetYourGuide** (planned): Bookable experiences
- **Internet Search** (planned): General public information and inspiration

Itineraries are personalized based on the destination, story/inspiration, traveler preferences, trip duration and date, and traveler type.

---

## Features

- Aggregate activities from multiple sources
- Prioritize agency bookable activities
- Filter activities by preferences, weather/seasonality, and traveler style
- Generate day-by-day itineraries for user's trip

---

## Planned Enhancements

- Integrate Tripadvisor and GetYourGuide APIs
- Add internet search enrichment for destination/story
- Expand data model to include preferences, seasonality, traveler suitability, and agency booking info
- Advanced filtering and prioritization logic

---

## Setup

1. Clone the repo
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables for external APIs (if needed)
4. Start the Flask app:
   ```bash
   python app.py
   ```

---

## API Usage

Send a POST request to `/generate_itinerary` with a payload like:

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

---

## Documentation

- [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md): Step-by-step development guide
- [DATA_MODEL.md](DATA_MODEL.md): Activity data structure
- [API_DESIGN.md](API_DESIGN.md): API endpoints and payloads
- [EXTERNAL_SOURCES.md](EXTERNAL_SOURCES.md): Integration strategies for external data
- [FILTERING_PRIORITIZATION.md](FILTERING_PRIORITIZATION.md): Filtering and prioritization logic

---

## License

MIT License

---

## Contributing

Pull requests and suggestions are welcome! See [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md) for open development steps.