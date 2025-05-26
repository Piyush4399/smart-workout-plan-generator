import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import streamlit as st

# Load local .env file (for local development)
load_dotenv()

# Get OpenAI API key - prioritize Streamlit secrets in deployment
api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

# Set up OpenAI client
client = openai.OpenAI(api_key=api_key)

# Flask app
app = Flask(__name__)

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    try:
        data = request.json
        age = data.get("age")
        weight = data.get("weight")
        height = data.get("height")
        goal = data.get("goal")

        prompt = (
            f"Create a weekly personalized workout plan for someone who is {age} years old, weighs {weight} kg, "
            f"is {height} cm tall, and wants to {goal.lower()}. Make it easy to understand, and format it as a bullet list by day."
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=700
        )

        plan = response.choices[0].message.content.strip()
        return jsonify({"plan": plan})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
