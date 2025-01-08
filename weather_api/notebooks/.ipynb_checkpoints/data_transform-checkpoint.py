import pandas as pd

# Path to the CSV file
file_path = "/Users/sa26/Documents/GitHub/Weather-API-Data-Engineering/weather_api/data/csv/weather_data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)
df.head()/df.tail()