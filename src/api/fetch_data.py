from src.config import LYFTA_API_KEY
import requests
import json

class FetchData:

    def __init__(self):
        self.token = LYFTA_API_KEY
        self.url = "https://my.lyfta.app/api/v1/workouts?limit=100"
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def fetch_workouts(self):
        response = requests.get(self.url, headers=self.headers)
        response.raise_for_status()
        
        # Save json file
        with open("src/data/json_data.json", "w") as f:
            json.dump(response.json(), f, indent=4)
        
        return response.json()

    def fetch_exercises(self):
        url = "https://my.lyfta.app/api/v1/exercises?limit=100"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        
        # Save json file
        with open("src/data/json_exercises.json", "w") as f:
            json.dump(response.json(), f, indent=4)
        
        return response.json()
