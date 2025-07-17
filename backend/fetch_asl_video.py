import requests

SIGN_ASL_API_URL = "https://www.signasl.org/sign/"

def get_asl_video(word):
    """
    Fetch ASL video URL from SignASL API for a given word.
    """
    try:
        response = requests.get(f"{SIGN_ASL_API_URL}{word}", timeout=5)
        if response.status_code == 200:
            # Extract video URL from the response
            return response.url  # SignASL redirects to the video page
        else:
            print(f"Error: No video found for {word}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None
