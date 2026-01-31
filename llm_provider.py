import os, json, re
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def extract_json(text):
    try:
        return json.loads(text)
    except:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {"error": "Invalid JSON", "raw": text}


def ask_llm(prompt):
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
        config={"response_mime_type": "application/json"}
    )
    return extract_json(response.text)
