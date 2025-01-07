import requests
import json
r = requests.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure")
data = r.json()
file_path = "/Users/sa26/Documents/GitHub/Weather-API-Data-Engineering/weather_api/data/json/weather_data.json"
with open(file_path, "w") as f:
    json.dump(data, f, indent=4) 
