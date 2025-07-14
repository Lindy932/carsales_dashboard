import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load your data
file_path = 'cars.csv'
df = pd.read_csv(file_path)

### Parallel Coordinates Data Preparation ###
# Select attributes for parallel coordinates
attributes = ['price', 'horsepower', 'enginesize', 'curbweight', 'citympg', 'highwaympg']
all_attributes = attributes + ['drivewheel', 'carbody']

# Copy the selected columns
parallel_data = df[all_attributes].copy()

# Standardize the numerical attributes for parallel coordinates
scaler = StandardScaler()
parallel_data[attributes] = scaler.fit_transform(parallel_data[attributes])

# Save the standardized data for parallel coordinates to a CSV file
parallel_data.to_csv('parallel_coordinates_data.csv', index=False)

print("Data preparation complete. File saved: 'parallel_coordinates_data.csv'")
