import requests
import json

token = "8932168d363cc4fd99402bf906e74083ed57d2261ba8d1b9bb3b4e3be25eb2d9"
url = "https://my.lyfta.app/api/v1/workouts?limit=100"
headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://my.lyfta.app/api/v1/exercises?limit=100?"
page = 1

response = requests.get(url + f"&page={page}", headers=headers)
response.raise_for_status()

while response.count != 0:
    page += 1
    time.sleep(2.5)  # Delay to avoid hitting rate limits
    next_page = requests.get(url + f"&page={page}", headers=headers)
    next_page.raise_for_status()
    response.extend(next_page.json())

# Save json file
with open("json_exercises.json", "w") as f:
    json.dump(response.json(), f, indent=4) 

