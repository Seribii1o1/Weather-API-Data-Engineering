import pandas as pd
# Load the data from the CSV file
df = pd.read_csv('/Users/sa26/Documents/GitHub/Weather-API-Data-Engineering/weather_api/data/csv/weather_data.csv').dropna() 
df['time'] = pd.to_datetime(df['time'])
df['month'] = df['time'].dt.month
df['year'] = df['time'].dt.year
monthly_medians = df.groupby('month')[['temperature_2m', 'relative_humidity_2m', 'precipitation', 'surface_pressure']].median()
yearly_medians = df.groupby('year')[['temperature_2m', 'relative_humidity_2m', 'precipitation', 'surface_pressure']].median()
print(monthly_medians)
print(yearly_medians)
harvest_df = pd.read_csv('/Users/sa26/Documents/GitHub/Weather-API-Data-Engineering/weather_api/data/csv/br_final.csv').dropna() 
minas_harvest = harvest_df[harvest_df['subdivision'] == 'Minas Gerais']
yearly_medians_harvest = minas_harvest.groupby('year')[['million_60kgs_bag', 'nonbear_mill_trees', 'bear_mill_trees', 'avg_unemp_perc']].median()
# Merge the dataframes on the year
merged_data = pd.merge(yearly_medians, yearly_medians_harvest, on='year')
# Display the merged dataframe
print(merged_data)
file_path1 = "/Users/sa26/Documents/GitHub/Weather-API-Data-Engineering/weather_api/data/csv/monthly_medians.csv"
monthly_medians.to_csv(file_path1, index=False)
file_path2 = "/Users/sa26/Documents/GitHub/Weather-API-Data-Engineering/weather_api/data/csv/yearly_medians.csv"
yearly_medians.to_csv(file_path2, index=False)
file_path3 = "/Users/sa26/Documents/GitHub/Weather-API-Data-Engineering/weather_api/data/csv/merged_data.csv"
merged_data.to_csv(file_path3, index=False)