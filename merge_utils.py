def merge_and_deduplicate(agency_data, llm_data):
    # Build set of (story, location, tuple(activities)) for agency data
    agency_keys = set(
        (entry["story"], entry["location"], tuple(entry["activities"])) for entry in agency_data
    )
    results = []
    # Add all agency data first
    for entry in agency_data:
        entry_copy = entry.copy()
        entry_copy["source"] = "agency"
        results.append(entry_copy)
    # Add LLM data only if not present in agency data
    for entry in llm_data:
        key = (entry["story"], entry["location"], tuple(entry["activities"]))
        if key not in agency_keys:
            entry_copy = entry.copy()
            entry_copy["source"] = "llm"
            results.append(entry_copy)
    return results