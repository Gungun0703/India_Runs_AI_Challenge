import json
import pandas as pd

FILE_PATH = r"data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

TARGET_SKILLS = [
    "Milvus",
    "Qdrant",
    "Weaviate",
    "Pinecone",
    "FAISS",
    "Elasticsearch",
    "OpenSearch",
    "Embeddings",
    "RAG",
    "Retrieval",
    "Ranking",
    "LLM",
    "Fine-tuning LLMs",
    "NLP",
    "Python"
]

PROFICIENCY_WEIGHT = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3
}

rows = []

with open(FILE_PATH, "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        skills = candidate.get("skills", [])

        skill_score = 0

        for skill in skills:

            name = skill.get("name", "")

            if name in TARGET_SKILLS:

                prof = skill.get("proficiency", "beginner")
                endorsements = skill.get("endorsements", 0)
                duration = skill.get("duration_months", 0)

                skill_score += (
                    10 * PROFICIENCY_WEIGHT.get(prof, 1)
                )

                skill_score += min(endorsements, 50) / 10
                skill_score += min(duration, 60) / 12

        years = candidate["profile"]["years_of_experience"]
        experience_score = min(years, 10)

        signals = candidate["redrob_signals"]

        behavior_score = (
            signals["recruiter_response_rate"] * 25
            + signals["interview_completion_rate"] * 25
            + signals["offer_acceptance_rate"] * 20
            + signals.get("github_activity_score", 0)
            + signals.get("saved_by_recruiters_30d", 0)
            + signals.get("search_appearance_30d", 0) / 100
        )

        final_score = (
            0.5 * skill_score
            + 0.2 * experience_score
            + 0.3 * behavior_score
        )

        rows.append({
            "candidate_id": candidate["candidate_id"],
            "score": round(final_score, 2)
        })

df = pd.DataFrame(rows)

df = df.sort_values(
    by="score",
    ascending=False
)

df["rank"] = range(
    1,
    len(df) + 1
)

print(df.head(20))
top100 = df.head(100).copy()

top100["reasoning"] = (
    "Strong alignment with AI Engineer requirements through relevant AI/LLM skills, experience, endorsements, and positive recruiter engagement signals."
)

submission = top100[
    ["candidate_id", "rank", "score", "reasoning"]
]

submission.to_csv(
    "top100_submission.csv",
    index=False
)

print("Submission file created successfully!")
print(submission.head())