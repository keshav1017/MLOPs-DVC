import pandas as pd
import os

# create a sample DataFrame with column names
data = {"Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"]}

df = pd.DataFrame(data)

# adding new row to df for v2
new_row_loc1 = {"Name": "GF1", "Age": 20, "City": "City1"}
df.loc[len(df.index)] = new_row_loc1

# # adding new row to df for v3
# new_row_loc2 = {"Name": "V3", "Age": 30, "City": "City2"}
# df.loc[len(df.index)] = new_row_loc2

# Ensure Data directory exits in root level
data_dir = "data"
os.makedirs(data_dir, exist_ok = True)

# Define file path
file_path = os.path.join(data_dir, "sample_data.csv")

# Save data to csv file, including column names
df.to_csv(file_path, index = False)

print(f"CSV file saved to {file_path}")