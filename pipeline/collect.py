from pipeline.agency import fetch_agency_activities
from pipeline.kultrip import fetch_kultrip_activities
from pipeline.external import fetch_external_activities
# If you have generate_llm_suggestions, import it from its correct module

def collect(destination, preferences=None, inspiration=None):
    activities = []
    activities += fetch_agency_activities(destination, preferences)
    activities += fetch_kultrip_activities(destination, preferences)
    activities += fetch_external_activities(destination, preferences)
    # activities += generate_llm_suggestions(destination, preferences)  # If available

    # Tag activities that match the inspiration
    if inspiration:
        tag = inspiration.lower().strip()
        for act in activities:
            story_tags = [t.lower() for t in act.get("story_tags", [])]
            act['story_match'] = tag in story_tags
    else:
        for act in activities:
            act['story_match'] = False

    return activities