from pipeline.storytelling import generate_storytelling

def build_itinerary(activities, duration=3, inspiration=None, language="en"):
    print(f"[ITINERARY] Building itinerary with duration {duration} days and inspiration '{inspiration}'")
    itinerary = []
    activity_slots = ["morning", "afternoon", "evening"]
    total_needed = duration * len(activity_slots)
    # Prioritize story_match activities
    story_acts = [a for a in activities if a.get("story_match")]
    other_acts = [a for a in activities if not a.get("story_match")]
    selected_activities = story_acts + other_acts
    selected_activities = selected_activities[:total_needed]

    for day in range(duration):
        day_plan = {"day": day + 1}
        for i, slot in enumerate(activity_slots):
            idx = day * len(activity_slots) + i
            if idx < len(selected_activities):
                activity = selected_activities[idx].copy()
                activity["slot"] = slot
                activity["storytelling"] = generate_storytelling(activity, inspiration)
                print(f"[ITINERARY] Assigned '{activity['activity']}' to day {day+1} ({slot})")
                day_plan[slot] = activity
            else:
                day_plan[slot] = None
        itinerary.append(day_plan)
    print(f"[ITINERARY] Itinerary built with {duration} days x 3 slots.")
    return {"itinerary": itinerary}