import pandas as pd
import json

with open("../data/evaluated.json") as f:
    data = json.load(f)

rows = []

for item in data:
    row = {
        "id": item["id"],
        "prompt": item["prompt"],
        "accuracy": item["scores"]["accuracy"],
        "relevance": item["scores"]["relevance"],
        "clarity": item["scores"]["clarity"],
        "total": item["scores"]["total"]
    }
    rows.append(row)

df = pd.DataFrame(rows)
df["label"] = df["total"].apply(lambda x: "good" if x >= 2 else "bad")

# Print summary
print("\nAverage Scores:")
print(df.mean(numeric_only=True))

print("\nLow Quality Responses:")
print(df[df["total"] < 2])

# Save full analysis
df.to_csv("../data/analysis.csv", index=False)

# Save summary separately
summary = {
    "avg_accuracy": df["accuracy"].mean(),
    "avg_relevance": df["relevance"].mean(),
    "avg_clarity": df["clarity"].mean(),
    "avg_total": df["total"].mean()
}

with open("../data/summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("\nAnalysis saved to data/analysis.csv and data/summary.json")