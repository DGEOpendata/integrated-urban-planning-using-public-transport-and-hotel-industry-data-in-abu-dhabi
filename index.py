python
import pandas as pd

# Load the public transportation dataset
transport_data = pd.read_csv('path_to_public_transport_data.csv')

# Load the hotel occupancy dataset
hotel_data = pd.read_excel('path_to_hotel_data.xlsx')

# Merge datasets on a common key, for example, 'date'
data_combined = pd.merge(transport_data, hotel_data, on='date')

# Example analysis: Determine peak transport usage during high hotel occupancy
peak_transport_usage = data_combined[(data_combined['hotel_occupancy_rate'] > 80) & (data_combined['peak_hours'] == True)]

# Output the analysis
print("Peak Transport Usage during High Hotel Occupancy:")
print(peak_transport_usage[['date', 'ridership', 'hotel_occupancy_rate']])

# Further analysis can follow based on specific urban planning queries
