def fetch_agency_activities(destination):
    if destination.lower() == "london":
        return [
            {
                "activity": "Harry Potter Studio Tour",
                "location": "Leavesden",
                "description": "Experience the magic behind the Harry Potter films.",
                "story_tags": ["harry potter", "book", "magic", "fantasy"],
            },
            {
                "activity": "Sherlock Holmes Museum Visit",
                "location": "Baker Street",
                "description": "Explore the world of Sherlock Holmes at 221B Baker Street.",
                "story_tags": ["sherlock holmes", "book", "detective", "victorian london"],
            },
            # ... more activities ...
        ]
    # ... handle other destinations ...
    return []