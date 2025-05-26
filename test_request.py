import requests

url = "http://127.0.0.1:5000/generate-plan"

payload = {
    "age": 26,
    "weight": 72,
    "height": 178,
    "goal": "lose fat"
}

response = requests.post(url, json=payload)

print("\n🧠 Workout Plan:\n")
print(response.json().get("plan", "Something went wrong"))
