import streamlit as st
import pandas as pd

def dashboard(df):

    st.header("Training Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Workouts", df["workout_id"].nunique())
    col2.metric("Total Volume (lbs)", round(df["volume"].sum(), 0))
    col3.metric("Exercises Logged", df["exercise"].nunique())

    st.subheader("📈 Volume Over Time")
    daily = df.groupby("date")["volume"].sum()
    st.line_chart(daily)

    st.subheader("📊 Total Workouts by Week")
    weekly = df.groupby("week")["workout_id"].nunique()
    st.bar_chart(weekly, x_label="Week #", y_label="Total Workouts")

    st.subheader("💪 Top Exercises")
    top = df.groupby("exercise")["volume"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top)