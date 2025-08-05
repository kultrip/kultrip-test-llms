from flask import Flask, request, jsonify
from utils.auth import validate_user
from utils.credits import check_credits, deduct_credits
from pipeline.collect import collect
from pipeline.normalize import normalize
from pipeline.deduplicate import deduplicate
from pipeline.enrich import enrich
from pipeline.filter import filter_activities
from pipeline.prioritize import prioritize
from pipeline.itinerary import build_itinerary
from pipeline.translate import translate

app = Flask(__name__)

@app.route('/generate_itinerary', methods=['POST'])
def generate_itinerary():
    data = request.json
    user_token = data.get("user_token")
    destination = data.get("destination")
    preferences = data.get("preferences", {})
    inspiration = data.get("inspiration")  # <---- NEW LINE: get inspiration from request
    language = data.get("language", "en")
    duration = data.get("duration", 3)

    # 1. Authenticate user and check credits
    user = validate_user(user_token)
    if not user:
        return jsonify(error="Invalid user"), 401
    if not check_credits(user["id"], duration):
        return jsonify(error="Insufficient credits"), 402

    # 2. Pipeline steps
    raw_data = collect(destination, preferences, inspiration)  # <---- PASS inspiration to collect
    normalized = normalize(raw_data)
    deduped = deduplicate(normalized)
    enriched = enrich(deduped)
    filtered = filter_activities(enriched, preferences)
    prioritized = prioritize(filtered, preferences)
    itinerary = build_itinerary(prioritized, duration, inspiration=inspiration)  # <---- PASS inspiration

    # 3. Translate if needed
    if language != "en": 
        itinerary = translate(itinerary, language)

    # 4. Deduct credits
    deduct_credits(user["id"], duration)

    return jsonify(itinerary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)