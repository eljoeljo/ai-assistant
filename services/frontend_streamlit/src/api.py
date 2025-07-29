import requests

def gemini_api_call(api_key: str, prompt: str):
    """A request is built and then sent to Gemini API. The 
    API sends a response which is then parsed and returned.

    Args:
        api_key (str): Gemini API Key
        prompt (str): User input
    """
    url = ( # Defining the REST endpoint and headers
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-2.5-flash:generateContent"
    )

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": api_key,    # alternative to ?key= in URL
    }
    
    body = {
    "contents": [
        {
            "parts": [
                {"text": f"{prompt}"}
            ]
        }
    ]
}
    # Sending the request
    resp = requests.post(url, headers=headers, json=body, timeout=30)
    
    # Receiving and parsing response
    resp.raise_for_status()
    data = resp.json()
    candidates = data.get("candidates", [])
    
    return candidates
