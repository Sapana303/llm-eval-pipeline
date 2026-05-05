# LLM Response Evaluation & Benchmarking System

## Overview
This project implements a complete evaluation pipeline for Large Language Models (LLMs), simulating real-world post-training workflows used in AI systems. It generates responses using a local LLM, evaluates them using a structured rubric, and produces quantitative insights for performance analysis.

## Key Features

- Prompt → Response generation using Ollama (local LLM)
- Rubric-based evaluation:
  - Accuracy
  - Relevance
  - Clarity
- Automated scoring system
- Structured outputs (JSON + CSV)
- Performance analysis & failure detection

## Tech Stack

- Python
- Pandas
- Ollama
- JSON / CSV

## Evaluation Framework

Each response is scored on:

| Metric     | Description                          |
|------------|--------------------------------------|
| Accuracy   | Matches expected/reference answer    |
| Relevance  | Answers the question                 |
| Clarity    | Concise and understandable           |

**Score Range:** 0–3

## Sample Output

- `analysis.csv` → Detailed scoring per response  
- `summary.json` → Aggregated metrics  

## How to Run
1. Install dependencies
bash
pip install -r requirements.txt
2. Start LLM
bash
ollama run llama3
3. Run pipeline
bash
cd src
python generate.py
python evaluate.py
python analyze.py

## Future Improvements
Multi-response ranking (best vs worst)

Human vs automated evaluation comparison

Integration with LangSmith

Advanced scoring (semantic similarity instead of keyword match)
