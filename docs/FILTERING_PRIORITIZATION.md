# Filtering & Prioritization Logic

## **Filtering Steps**

1. **By Destination**: Only activities in the target location.
2. **By Story**: Activities inspired by the story/inspiration.
3. **By Preferences**: Prioritize activities matching traveler's interests.
4. **By Traveler Style/Number**: Fit for solo, couple, family, business.
5. **By Seasonality/Weather**: Fit for trip date/season.

## **Prioritization Hierarchy**

1. **Agency Bookable Activities**
2. **Preference Match**
3. **Story Inspiration**
4. **Weather/Seasonality Match**
5. **Traveler Suitability**
6. **Source Trust (agency > kultrip > tripadvisor > internet > LLM)**

## **Itinerary Building**

- Fill each day with top-priority activities.
- Ensure variety and logical order (don't repeat same activity type).
- Provide booking info if available.
- If possible, suggest alternatives for weather or preferences.

## **Sample Filtering Function (Python)**

```python
def filter_and_prioritize_activities(all_activities, preferences, duration, date_of_trip, traveler_style):
    preferred = [a for a in all_activities if set(a.get("preferences", [])) & set(preferences)]
    suitable = [a for a in preferred if traveler_style in a.get("suitable_for", [])]
    season = get_season(date_of_trip)
    seasonal = [a for a in suitable if season in a.get("seasonality", [])]
    agency_first = sorted(seasonal, key=lambda x: not x.get("available_through_agency", False))
    return agency_first[:duration]
```

## **Weather/Seasonality Helpers**

```python
def get_season(date):
    month = date.month
    # Return "summer", "autumn", etc. based on month
```