from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import openai

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def home():
    return "Smart Workout Plan Generator API is running!"

@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    data = request.get_json()

    age = data.get("age")
    weight = data.get("weight")
    height = data.get("height")
    goal = data.get("goal")

    prompt = f"""
    Create a personalized weekly workout plan for someone who is:
    - Age: {age}
    - Weight: {weight} kg
    - Height: {height} cm
    - Goal: {goal}

    Include recommended days of training, type of workouts (strength, cardio, flexibility), and a sample weekly split.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional fitness coach."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=400
        )

        plan = response.choices[0].message.content
        return jsonify({"plan": plan})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
