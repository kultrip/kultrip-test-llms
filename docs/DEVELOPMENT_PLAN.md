# Development Plan for Multi-Source Itinerary Generator

## **Project Goal**
Build an itinerary generator that combines data from multiple sources (internet, Tripadvisor, GetYourGuide, Kultrip, agency, LLMs) and prioritizes activities according to agency availability, traveler preferences, inspiration/story, weather, and trip parameters.

---

## **Development Steps**

### **1. Data Model Enhancement**
- Update `agency_data.py`, `kultrip_data.py`, etc. to include fields:
  - `preferences`: List of relevant traveler interests (e.g. `"sports"`, `"arts"`)
  - `available_through_agency`: Boolean
  - `suitable_for`: List (`"solo"`, `"family"`, etc.)
  - `seasonality`: List of months/seasons
  - (Optional) `price`, `booking_url`, etc.

### **2. API Input Update**
- Accept these fields in itinerary generation endpoint:
  - `destination`
  - `story`
  - `preferences` (list)
  - `duration` (days)
  - `date_of_trip`
  - `number_of_travelers`
  - `traveler_style` (solo, couple, family, business)

### **3. External Source Integration**
- **Internet**: Implement a search step (Bing, Google, etc.) for `"destination"+"story"`.
- **Tripadvisor**: Integrate API or scraping for activities, tours, events.
- **GetYourGuide**: Integrate API or scraping for bookable experiences.

### **4. Data Aggregation**
- Gather activities from all sources.
- Tag each entry with its source.

### **5. Filtering & Prioritization**
- Filter all activities by:
  - Destination
  - Story/inspiration
  - Preferences
  - Traveler style/number
  - Seasonality/weather
- Prioritize:
  1. Agency bookable activities
  2. Preference match
  3. Story relevance
  4. Weather suitability
  5. Traveler style suitability

### **6. Itinerary Construction**
- Fill itinerary for the entire trip duration.
- Assign activities to each day.
- Ensure variety and logical distribution.

### **7. Output Format**
- Each day’s activities, with source, agency booking info, and fit for preferences, weather, and traveler type.

---

## **Documentation**
- See sub-documents for details:
  - [DATA_MODEL.md](DATA_MODEL.md): Data structure for activities
  - [API_DESIGN.md](API_DESIGN.md): API endpoints and sample payloads
  - [EXTERNAL_SOURCES.md](EXTERNAL_SOURCES.md): Integration strategies for internet, Tripadvisor, GetYourGuide
  - [FILTERING_PRIORITIZATION.md](FILTERING_PRIORITIZATION.md): Logic for filtering and prioritizing activities

---

## **Next Steps**
- Refine data models and update backend stubs
- Research and prototype API integration for external sources
- Build filtering/prioritization logic
- Test and iterate!