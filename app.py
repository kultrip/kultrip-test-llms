from flask import Flask, request, jsonify
from llms import run_llm_for_story
from agency_data import AGENCY_DATA
from merge_utils import merge_and_deduplicate

app = Flask(__name__)

@app.route("/generate_story", methods=["POST"])
def generate_story():
    data = request.json
    story = data.get("story")
    destination = data.get("destination")

    if not story or not destination:
        return jsonify(error="Missing 'story' or 'destination'"), 400

    llm_data = run_llm_for_story(story, destination)
    agency_data_filtered = [entry for entry in AGENCY_DATA if entry["story"] == story]
    combined = merge_and_deduplicate(agency_data_filtered, llm_data)

    return jsonify(combined)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)