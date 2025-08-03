def merge_and_deduplicate(all_entries):
    """
    Deduplicate entries based on (story, location, tuple(activities)).
    Keeps the first occurrence from any source.
    """
    deduped = []
    seen = set()
    for entry in all_entries:
        key = (entry["story"], entry["location"], tuple(entry["activities"]))
        if key not in seen:
            seen.add(key)
            deduped.append(entry)
    return deduped