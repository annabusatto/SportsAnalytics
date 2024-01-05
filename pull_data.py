import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
print(api_key)

url = "https://api.collegefootballdata.com/games"
headers = {"Accept": "application/json", "Authorization": f"Bearer {api_key}"}
params = {"year": 2022, "seasonType": "regular"}
response = requests.get(url, headers=headers, params=params)
print(response.status_code)
# df = pd.read_json(response.text)
df = pd.json_normalize(
    response.json()
)  # dataframe, json = java script object notation (file format)
df.columns = map(
    str.upper, df.columns
)  # change all the columns title to upper case letters, makes easier for SQL

print(df.head())  # print first 5 rows
df.to_csv("games.csv", index=False)
