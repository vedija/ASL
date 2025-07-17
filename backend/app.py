from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

def extract_video_url(word):
    asl_url = f"https://www.signasl.org/sign/{word}"
    response = requests.get(asl_url)
    
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    video_tag = soup.find("video")
    
    if video_tag:
        video_source = video_tag.find("source")
        if video_source:
            return video_source["src"]
    
    return None

@app.route("/convert", methods=["POST"])
def convert_text_to_asl():
    data = request.get_json()
    text = data.get("text", "").strip().lower()
    
    words = text.split()  # Split the text into individual words
    video_urls = []

    for word in words:
        video_url = extract_video_url(word)
        if video_url:
            video_urls.append({"word": word, "url": video_url})

    if video_urls:
        return jsonify({"videos": video_urls})
    else:
        return jsonify({"error": "No ASL videos found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
