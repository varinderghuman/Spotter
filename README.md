# Spotter — Workout Intelligence System

> A personalized fitness coach that analyzes workout history and generates adaptive training recommendations using data science and machine learning.

---

## Overview

**Spotter** is an end-to-end data science system that transforms raw workout logs into intelligent training recommendations.

The platform integrates workout tracking data from :contentReference[oaicite:0]{index=0}, processes structured exercise history, engineers training and recovery features, and generates personalized workout recommendations through a hybrid rule-based and machine learning pipeline.

Spotter was designed to demonstrate:
- Real-world API ingestion
- ETL and data pipeline engineering
- Feature engineering for behavioral/time-series data
- Recommendation systems
- Interactive ML applications with Streamlit

---

# Core Features

## Training Analytics Dashboard
- Workout frequency analysis
- Volume trends over time
- Exercise-level progression tracking
- Strength and workload visualization

## Personal Trainer
- Generates next workout recommendations
- Suggests progressive overload adjustments
- Estimates fatigue and recovery readiness
- Provides explainable recommendation reasoning

## Progress Analysis
- Exercise-specific strength trends
- Rolling workload analysis
- Performance plateau detection
- Historical training insights

## Data Explorer
- Interactive raw dataset inspection
- Exercise filtering and analysis
- Transparent access to engineered features

---

# System Architecture

```text
Lyfta API
    ↓
Raw JSON Workout Data
    ↓
ETL / Data Cleaning Pipeline
    ↓
Feature Engineering
    ↓
Recommendation Engine
    ↓
Streamlit Dashboard
```

---

# Tech Stack

## Core
- Python
- Pandas
- NumPy
- Scikit-learn

## Visualization
- Streamlit
- Plotly
- Matplotlib

## Data Engineering
- REST API Integration
- JSON Normalization
- CSV / Structured Dataset Pipelines

---

# Machine Learning & Feature Engineering

Spotter uses a hybrid recommendation architecture combining rule-based decision systems with machine learning.

## Engineered Features

### Time-Based Features
- Days since previous workout
- Workout frequency
- Weekly training distribution

### Progression Features
- Previous session weight/reps
- Rolling average volume
- Progressive overload tracking
- Volume delta trends

### Fatigue Features
- 7-day rolling workload
- Acute training load estimation
- Recovery readiness scoring

### Performance Features
- Total workout volume
- Estimated exercise intensity
- Historical progression metrics

---

# Recommendation System

The recommendation engine evaluates:

- Recovery status
- Recent training volume
- Exercise progression trends
- Fatigue accumulation
- Undertrained movement patterns

The system then generates:
- Recommended exercises
- Suggested load adjustments
- Training focus priorities

---

# Example Recommendation Output

```text
Next Workout Recommendation:

Focus: Chest + Triceps

Exercises:
- Bench Press → 135 lbs × 8 reps
- Cable Fly → 50 lbs × 12 reps
- Triceps Pushdown → 70 lbs × 10 reps

Reasoning:
- Chest not trained in 5 days
- Low fatigue score detected
- Previous session showed positive progression
```

---

# Project Structure

```text
Spotter/
│
├── app/
│   ├── streamlit_app.py
│   └── pages/
│       ├── 1_Dashboard.py
│       ├── 2_AI_Coach.py
│       ├── 3_Progress.py
│       └── 4_Data_Explorer.py
│
├── src/
│   ├── api/
│   │   └── lyfta_client.py
│   │
│   ├── data/
│   │   └── build_dataset.py
│   │
│   ├── features/
│   │   └── feature_builder.py
│   │
│   ├── model/
│   │   ├── recommender.py
│   │   ├── train_model.py
│   │   └── spotter_engine.py
│   │
│   └── config.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── notebooks/
├── tests/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# Installation

## Clone repository

```bash
git clone https://github.com/yourusername/spotter.git
cd spotter
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure environment variables

Create a `.env` file:

```env
LYFTA_API_KEY=your_api_key_here
```

---

## Run application

```bash
streamlit run app/streamlit_app.py
```

---

# Environment Variables

| Variable | Description |
|---|---|
| `LYFTA_API_KEY` | API token for Lyfta workout data |

---

# Future Improvements

- Conversational AI gym coach
- LLM-powered workout explanations
- Muscle fatigue heatmaps
- Workout PDF export
- Wearable integration
- Personalized recovery optimization

---

# What This Project Demonstrates

- End-to-end data pipeline engineering
- Real-world API integration
- Nested JSON normalization
- Feature engineering for time-series systems
- Hybrid recommendation systems
- Explainable machine learning workflows
- Interactive data application development
- Production-style Python project architecture

---

# Author

Built by **Varinder Singh**

Focus areas:
- Data Science
- Machine Learning Systems
- Analytics Engineering

---

# Acknowledgements

Workout data sourced through the Lyfta API.

---
