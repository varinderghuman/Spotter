import streamlit as st

def data_explorer(df):

    st.header("📂 Raw Data Explorer")

    st.dataframe(df)

    st.subheader("Filter by Exercise")

    ex = st.selectbox("Exercise", df["exercise"].unique())

    st.dataframe(df[df["exercise"] == ex])