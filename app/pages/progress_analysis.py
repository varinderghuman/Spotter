import streamlit as st

def progress_analysis(df):

    st.header("📈 Progress Analysis")

    exercise = st.selectbox("Select Exercise", df["exercise"].unique())

    subset = df[df["exercise"] == exercise]

    st.subheader("Weight Progression")
    st.line_chart(subset.set_index("date")["weight"])

    st.subheader("Volume Progression")
    subset["volume"] = subset["weight"] * subset["reps"]
    st.line_chart(subset.set_index("date")["volume"])

    st.subheader("Reps Trend")
    st.line_chart(subset.set_index("date")["reps"])