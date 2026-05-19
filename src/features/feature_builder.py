import pandas as pd
import numpy as np

class FeatureBuilder:

    def __init__(self, df):
        self.df = df.copy()

    def preprocess(self):
        self.df["date"] = pd.to_datetime(self.df["date"])
        self.df["weight"] = pd.to_numeric(self.df["weight"], errors="coerce")
        self.df["reps"] = pd.to_numeric(self.df["reps"], errors="coerce")
        self.df["volume"] = self.df["weight"] * self.df["reps"]
        return self.df

    def time_features(self):
        self.df = self.df.sort_values("date")
        self.df["weekday"] = self.df["date"].dt.weekday
        self.df["week"] = self.df["date"].dt.isocalendar().week.astype(int)
        return self.df

    def history_features(self):
        self.df["prev_weight"] = self.df.groupby("exercise")["weight"].shift(1)
        self.df["prev_reps"] = self.df.groupby("exercise")["reps"].shift(1)
        self.df["prev_volume"] = self.df.groupby("exercise")["volume"].shift(1)
        return self.df

    def rolling_features(self):
        self.df["roll3"] = (
            self.df.groupby("exercise")["volume"]
            .rolling(3, min_periods=1)
            .mean()
            .reset_index(level=0, drop=True)
        )
        return self.df

    def fatigue_features(self):
        self.df["daily_volume"] = self.df.groupby("date")["volume"].transform("sum")
        self.df["fatigue"] = (
            self.df.groupby("exercise")["daily_volume"]
            .rolling(7, min_periods=1)
            .sum()
            .reset_index(level=0, drop=True)
        )
        return self.df

    def build(self):
        self.preprocess()
        self.time_features()
        self.history_features()
        self.rolling_features()
        self.fatigue_features()

        self.df = self.df.fillna(0)
        return self.df