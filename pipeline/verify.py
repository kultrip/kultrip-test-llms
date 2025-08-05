import os
import requests
from dotenv import load_dotenv

load_dotenv()
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def verify_activity(activity):
    query = f"{activity['location']} {activity.get('activity', '')} {activity.get('source', '')}"
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "key": GOOGLE_MAPS_API_KEY
    }
    print(f"[VERIFY] Checking activity: {activity['activity']} at {activity['location']} ...")
    try:
        resp = requests.get(url, params=params, timeout=5)
        data = resp.json()
        print(f"[VERIFY] Google Places status: {data.get('status')}.")
        if data.get("results"):
            print(f"[VERIFY] Match found: {data['results'][0]['name']}")
        else:
            print(f"[VERIFY] No match found for '{query}'")
        verified = bool(data.get("results"))
        activity["verified"] = verified
        activity["verification_details"] = {
            "google_places_status": data.get("status"),
            "matched_name": data["results"][0]["name"] if data.get("results") else None
        }
        return activity
    except Exception as e:
        print(f"[ERROR] Verification failed for '{query}': {e}")
        activity["verified"] = False
        activity["verification_details"] = {"error": str(e)}
        return activity