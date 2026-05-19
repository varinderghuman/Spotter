from api.fetch_data import FetchData
from data.build_dataset import build_dataset
from features.feature_builder import FeatureBuilder
from model.recommender import WorkoutRecommender

class SpotterEngine:

    def __init__(self, token):
        self.client = FetchData(token)

    def run(self):

        raw = self.client.fetch_workouts()
        df = build_dataset(raw)

        features = FeatureBuilder(df).build()

        recommender = WorkoutRecommender(features)

        return recommender.recommend(), features