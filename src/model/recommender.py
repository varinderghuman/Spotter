import numpy as np

class WorkoutRecommender:

    def __init__(self, df):
        self.df = df

        self.vol_threshold = np.percentile(df["roll3"], 30)
        self.fatigue_threshold = np.percentile(df["fatigue"], 50)

    def score(self, row):

        score = 0

        if row["roll3"] < self.vol_threshold:
            score += 2

        if row["fatigue"] < self.fatigue_threshold:
            score += 1

        if row["weight_delta"] > 0:
            score += 1

        return score

    def recommend(self):

        df = self.df.copy()
        df["score"] = df.apply(self.score, axis=1)

        return (
            df.groupby("exercise")["score"]
            .mean()
            .sort_values(ascending=False)
            .head(3)
        )