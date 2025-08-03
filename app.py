from flask import Flask, request, jsonify
from agency_data import AGENCY_DATA
from kultrip_data import KULTRIP_DATA
from llms import run_gemini_for_story, run_openai_for_story
from merge_utils import merge_and_deduplicate

app = Flask(__name__)

@app.route("/generate_story", methods=["POST"])
def generate_story():
    data = request.json
    story = data.get("story")
    destination = data.get("destination")
    llm_choice = data.get("llm", "gemini")  # Default to gemini if not provided

    if not story or not destination:
        return jsonify(error="Missing 'story' or 'destination'"), 400

    # Select LLM function
    if llm_choice == "openai":
        llm_data = run_openai_for_story(story, destination)
    elif llm_choice == "claude":
        llm_data = run_claude_for_story(story, destination)
    else:  # Default/fallback to gemini
        llm_data = run_gemini_for_story(story, destination)

    # Filter agency and kultrip data by story
    agency_data_filtered = [entry for entry in AGENCY_DATA if entry["story"] == story]
    kultrip_data_filtered = [entry for entry in KULTRIP_DATA if entry["story"] == story]

    # Tag each data source
    all_data = []
    for entry in agency_data_filtered:
        entry_copy = entry.copy()
        entry_copy["source"] = "agency"
        all_data.append(entry_copy)
    for entry in kultrip_data_filtered:
        entry_copy = entry.copy()
        entry_copy["source"] = "kultrip"
        all_data.append(entry_copy)
    for entry in llm_data:
        entry_copy = entry.copy()
        entry_copy["source"] = "llm"
        all_data.append(entry_copy)

    # Deduplicate across all sources
    combined = merge_and_deduplicate(all_data)

    return jsonify(combined)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)