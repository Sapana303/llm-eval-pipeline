import json
import requests

def get_response(prompt):
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    print(res.json())
    return res.json()["response"]

with open("../data/prompts.json", "w") as f:
    prompts = json.load(f)

results = []

for item in prompts:
    response = get_response(item["prompt"])

    results.append({
        "id": item["id"],
        "prompt": item["prompt"],
        "response": response,
        "reference": item["reference"]
    })

with open("../data/responses.json", "w") as f:
    json.dump(results, f, indent=2)

print("Responses generated!")
