from pipeline.agency import fetch_agency_activities
from pipeline.kultrip import fetch_kultrip_activities
from pipeline.external import fetch_external_activities
from pipeline.llm import generate_llm_suggestions

def collect(destination, preferences):
    print(f"[COLLECT] Gathering activities for destination: {destination}")
    activities = []
    activities += fetch_agency_activities(destination, preferences)
    activities += fetch_kultrip_activities(destination, preferences)
    activities += fetch_external_activities(destination, preferences)
    activities += generate_llm_suggestions(destination, preferences)
    # (fact-checking and other code here)
    return activities