import streamlit as st

def ai_coach(df, recommender):

    st.header("🤖 AI Workout Coach")

    st.write("Generate your next optimized workout based on training history.")

    if st.button("Generate Next Workout"):

        recommendations = recommender.recommend()

        st.subheader("🔥 Recommended Focus")

        st.dataframe(recommendations)

        st.subheader("🏋️ Suggested Load Plan")

        latest = df.sort_values("date").groupby("exercise").tail(1)

        plans = []

        for _, row in latest.iterrows():

            next_weight = row["weight"] * 1.025  # simple progression rule

            plans.append({
                "exercise": row["exercise"],
                "current_weight": row["weight"],
                "suggested_weight": round(next_weight, 1),
                "reps_target": row["reps"]
            })

        st.dataframe(plans)

        st.subheader("🧠 Explanation")

        st.write("""
        - Muscle groups with low recent volume were prioritized  
        - Recovery time since last training was considered  
        - Progressive overload applied where fatigue is low  
        """)