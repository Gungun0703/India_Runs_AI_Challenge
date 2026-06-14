
# India Runs 2026 – Data & AI Challenge

## Overview

This project develops an AI-driven candidate ranking system for the India Runs Data & AI Challenge. The objective is to identify and rank the most suitable candidates from a dataset of 100,000 candidate profiles using profile information, skills, experience, and behavioral signals.

## Problem Statement

Recruiters often receive thousands of applications for AI-related roles. Manual screening is time-consuming and inconsistent. This solution automates candidate ranking using a weighted scoring framework.

## Dataset

The dataset contains:

* Candidate profile information
* Career history
* Education details
* Skills and proficiency levels
* Certifications
* Languages
* Redrob behavioral signals

## Methodology

### Feature Engineering

The model evaluates candidates based on:

1. Relevant AI and ML skills
2. Skill proficiency levels
3. Skill endorsements
4. Experience duration
5. Years of professional experience
6. Recruiter engagement metrics
7. Interview completion rates
8. Offer acceptance rates
9. GitHub activity and profile visibility

### Scoring Formula

Final Score combines:

* Skill Score (50%)
* Experience Score (20%)
* Behavioral Score (30%)

Candidates are ranked in descending order of their final score.

## Technologies Used

* Python
* Pandas
* NumPy

## Output

The system generates a ranked list of candidates and exports the Top 100 recommendations in CSV format.

## Future Improvements

* Semantic skill matching using embeddings
* Job-description-aware ranking
* Explainable AI recommendations
* Learning-to-rank models

## Author

Gungun Garg
B.Tech Computer Science Engineering
RTU
