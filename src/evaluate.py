import json

def evaluate(response, reference):
    score = {}

    # Accuracy
    score["accuracy"] = 1 if reference.lower() in response.lower() else 0

    # Relevance
    score["relevance"] = 1 if len(response.strip()) > 0 else 0

    # Clarity (simple heuristic)
    score["clarity"] = 1 if len(response.split()) < 80 else 0

    score["total"] = score["accuracy"] + score["relevance"] + score["clarity"]

    return score

with open("../data/responses.json") as f:
    data = json.load(f)

evaluated = []

for item in data:
    scores = evaluate(item["response"], item["reference"])
    item["scores"] = scores
    evaluated.append(item)

with open("../data/evaluated.json", "w") as f:
    json.dump(evaluated, f, indent=2)

print("Evaluation complete!")