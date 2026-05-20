import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
import pandas as pd

from src.features.feature_builder import FeatureBuilder
from src.model.recommender import WorkoutRecommender
from src.api.fetch_data import FetchData
from src.data.build_dataset import build_dataset

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

st.title("Spotter")


# FETCH DATA
# ---------------------------
df = FetchData().fetch_workouts()

body_part_mapping = {
    1: "Thighs",
    2: "Chest",
    3: "Hips",
    4: "Back",
    5: "Upper Arms",
    6: "Shoulders",
    7: "Forearms",
    8: "Calves",
    9: "Neck",
    10: "Cardio",
    11: "Full body",
    12: "Waist",
    13: "Plyometrics",
    14: "Weightlifting",
    15: "Yoga",
    16: "Stretching",
    17: "Biceps",
    18: "Triceps",
    19: "Quadriceps",
    20: "Hamstrings"
}

target_muscles_mapping = {
    2: "Adductor Longus",
    3: "Adductor Magnus",
    4: "Biceps Brachii",
    5: "Brachialis",
    6: "Brachioradialis",
    7: "Deep Hip External Rotators",
    8: "Deltoid Anterior",
    9: "Deltoid Lateral",
    10: "Deltoid Posterior",
    11: "Erector Spinae",
    12: "Gastrocnemius",
    13: "Gluteus Maximus",
    14: "Gluteus Medius",
    15: "Gluteus Minimus",
    16: "Gracilis",
    17: "Hamstrings",
    18: "Iliopsoas",
    19: "Infraspinatus",
    20: "Latissimus Dorsi",
    21: "Levator Scapulae",
    22: "Obliques",
    23: "Pectineous",
    24: "Pectoralis Major Clavicular Head",
    25: "Pectoralis Major Sternal Head",
    26: "Popliteus",
    27: "Quadriceps",
    28: "Rectus Abdominis",
    29: "Sartorius",
    30: "Serratus Ante",
    31: "Serratus Anterior",
    32: "Soleus",
    33: "Splenius",
    34: "Sternocleidomastoid",
    35: "Subscapularis",
    36: "Tensor Fasciae Latae",
    37: "Teres Major",
    38: "Teres Minor",
    39: "Tibialis Anterior",
    40: "Transverse Abdominis",
    41: "Trapezius Lower Fibers",
    42: "Trapezius Middle Fibers",
    43: "Trapezius Upper Fibers",
    44: "Triceps Brachii",
    45: "Wrist Extensors",
    46: "Wrist Flexors"
}

exercises_df["body_part"] = exercises_df["body_part"].map(body_part_mapping)

df = build_dataset(df)


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
# NAVIGATION
# ---------------------------
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Next Workout", "Progress Analysis", "Data Explorer"]
)

# ---------------------------
# ROUTING
# ---------------------------
if page == "Dashboard":
    dashboard(df)

elif page == "Next Workout":
    ai_coach(df, recommender)

elif page == "Progress Analysis":
    progress_analysis(df)

elif page == "Data Explorer":
    data_explorer(df)
