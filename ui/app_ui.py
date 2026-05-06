import streamlit as st
import requests

st.title("🏨 AI Hotel Agent")

query = st.text_input("Ask your query")

if st.button("Search"):

    res = requests.get(
        "https://staybuddy-ai-agent.onrender.com/agent",
        params={"query": query}
    )

    data = res.json()

    if data.get("error"):
        st.error(data["error"])
    else:
        for h in data["result"]:
            st.write(
                f"🏨 {h['name']} | ⭐ {h['rating']} | "
                f"Check-in: {h['checkin']} | {h['status']}"
            )