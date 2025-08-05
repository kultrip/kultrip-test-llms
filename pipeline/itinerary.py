def build_itinerary(data, duration=3):
    print(f"[ITINERARY] Building itinerary with duration {duration} days")
    itinerary = []
    for i, activity in enumerate(data[:duration]):
        item = activity.copy()
        item["day"] = i + 1
        print(f"[ITINERARY] Assigned '{item['activity']}' to day {item['day']}")
        itinerary.append(item)
    print(f"[ITINERARY] Itinerary built with {len(itinerary)} activities.")
    return {"itinerary": itinerary}