# Extensibility: Adding New Data Sources & Agency Activities

## Adding External Sources

1. **Create a connector module** for the new source (e.g., `tripadvisor_connector.py`).
2. **Map source data** to the standardized activity model (see [DATA_MODEL.md](../DATA_MODEL.md)).
3. **Tag activities** with the source name.
4. **Integrate** the connector in the aggregation step for itinerary generation.

## Example Connector Skeleton

```python
# tripadvisor_connector.py
def get_activities(destination, preferences, date, duration):
    # Query Tripadvisor API or scrape site
    # Map results to standard activity schema
    return activities_list
```

## Agency Contribution Guide

- Agencies can provide activities via a CSV, API, or direct integration.
- Required fields: activity name, description, location, preferences, suitability, seasonality, booking URL.
- Activities should be mapped to the schema in [DATA_MODEL.md](../DATA_MODEL.md).

### Example Agency Activity Entry

```json
{
  "activity": "Vespa City Tour",
  "description": "Explore Rome on a vintage Vespa.",
  "location": "Rome",
  "preferences": ["adventure", "sightseeing"],
  "available_through_agency": true,
  "suitable_for": ["solo", "couple"],
  "seasonality": ["spring", "summer"],
  "booking_url": "https://agency.example.com/book/vespa-tour"
}
```

## Contributing New Sources

- Fork the repo and add your connector in `/sources/`.
- Submit a pull request with tests and documentation.
- See [DEVELOPMENT_PLAN.md](../DEVELOPMENT_PLAN.md) for roadmap and contribution guidelines.

---