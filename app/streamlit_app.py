import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
import pandas as pd

from src.features.feature_builder import FeatureBuilder
from src.model.recommender import WorkoutRecommender

from app.pages.dashboard import dashboard
from app.pages.ai_coach import ai_coach
from app.pages.progress_analysis import progress_analysis
from app.pages.data_explorer import data_explorer


# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Spotter",
    page_icon="🏋️",
    layout="wide"
)

st.title("🏋️ Spotter AI Coach")


# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_csv("src/data/workouts.csv")


# ---------------------------
# FEATURE ENGINEERING
# ---------------------------
builder = FeatureBuilder(df)
df = builder.build()


# ---------------------------
# MODEL
# ---------------------------
recommender = WorkoutRecommender(df)


# ---------------------------
# NAVIGATION (ONLY ONCE)
# ---------------------------
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "AI Coach", "Progress Analysis", "Data Explorer"]
)


# ---------------------------
# ROUTING
# ---------------------------
if page == "Dashboard":
    dashboard(df)

elif page == "AI Coach":
    ai_coach(df, recommender)

elif page == "Progress Analysis":
    progress_analysis(df)

elif page == "Data Explorer":
    data_explorer(df)