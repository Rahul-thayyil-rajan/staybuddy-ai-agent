import streamlit as st
import requests

st.title("🏨 AI Hotel Agent")

query = st.text_input("Ask your query")

if st.button("Search"):

    res = requests.get(
        "http://127.0.0.1:8000/agent",
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