import streamlit as st
import requests

# ------------------- Page Config -------------------
st.set_page_config(page_title="Smart Workout Plan Generator", layout="centered")

# ------------------- Header -------------------
st.markdown("<h1 style='text-align: center;'>🏋️ Smart Workout Plan Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your details below to receive a personalized weekly workout plan:</p>", unsafe_allow_html=True)
st.markdown("---")

# ------------------- Form -------------------
with st.form("workout_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("🔢 Age", min_value=10, max_value=100, step=1)
        weight = st.number_input("⚖️ Weight (kg)", min_value=30, max_value=200, step=1)
    with col2:
        height = st.number_input("📏 Height (cm)", min_value=100, max_value=250, step=1)
        goal = st.selectbox("🎯 Fitness Goal", ["Lose Fat", "Gain Muscle", "Maintain"])
    
    submitted = st.form_submit_button("🚀 Generate Plan")

# ------------------- API Call -------------------
if submitted:
    with st.spinner("🧠 Thinking... Generating your smart plan..."):
        try:
            response = requests.post("http://127.0.0.1:5000/generate-plan", json={
                "age": age,
                "weight": weight,
                "height": height,
                "goal": goal
            })
            result = response.json().get("plan", "No plan returned.")

            # Display nicely
            st.markdown("### 💡 Your Personalized Plan")
            st.markdown(
                f"<div style='background-color:#1e1e1e;padding:15px;border-radius:10px;color:#eee;'>"
                f"<pre style='white-space: pre-wrap; word-wrap: break-word;'>{result}</pre></div>",
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
