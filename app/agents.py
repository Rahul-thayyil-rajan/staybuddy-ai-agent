import json
import os
from groq import Groq
from dotenv import load_dotenv
from app.tools import search_hotels, get_checkin
from app.utils import normalize_time

load_dotenv()

print("KEY:", os.getenv("GROQ_API_KEY"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_info(query):
    prompt = f"""
Extract:
- location
- arrival_time (24hr HH:MM)

Return ONLY JSON.

Query: {query}
"""

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        content = res.choices[0].message.content.strip()
        content = content.replace("```json", "").replace("```", "")
        return json.loads(content)
    except:
        return None


def smart_agent(query):
    try:
        data = extract_info(query)

        if not data:
            return {"result": [], "error": "Could not understand query"}

        location = data.get("location")
        arrival_time_raw = data.get("arrival_time")

        if not location or not arrival_time_raw:
            return {"result": [], "error": "Missing location or time"}

        arrival_time = normalize_time(arrival_time_raw)

        hotels = search_hotels(location)

        results = []

        for h in hotels:
            checkin = get_checkin(h["hotel_id"])
            checkin_time = normalize_time(checkin)

            status = (
                "Available at arrival"
                if checkin_time <= arrival_time
                else "Check-in later"
            )

            results.append({
                "name": h["hotel_name"],
                "rating": h["review_score"],
                "checkin": checkin,
                "status": status
            })

        return {"result": results, "error": None}

    except Exception as e:
        return {"result": [], "error": str(e)}
    
   