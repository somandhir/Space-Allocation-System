import pandas as pd
import json
import base64

# C:/Users/91946/OneDrive/Desktop/WebD Projects/space allocation project/uploads
# Paths to the CSV and JSON files
csv_file_path = 'C:/Users/91946/OneDrive/Desktop/WebD Projects/space allocation project/uploads/items.csv'
json_file_path = 'C:/Users/91946/OneDrive/Desktop/WebD Projects/Data/column_mapping.json'
csv_store_path = 'C:/Users/91946/OneDrive/Desktop/WebD Projects/Data/csv_store.csv'
# excel_store_path = 'C:/Users/91946/OneDrive/Desktop/WebD Projects/Data/csv_store.xlsx'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Read the JSON file to get the column mapping
with open(json_file_path, 'r') as json_file:
    column_mapping = json.load(json_file)

# Ensure all required columns are present, if not, add them with default value 0
for expected_col, actual_col in column_mapping.items():
    if actual_col not in df.columns:
        df[actual_col] = 0

# Extract the required columns using the mapping and rename them to expected_col
extracted_data = df.rename(columns=column_mapping)[list(column_mapping.values())]
extracted_data.columns = list(column_mapping.keys())
# extracted_data.to_excel(excel_store_path, index=False)

# Encode the 'name' column (or any other column) into an integer
if 'name' in extracted_data.columns:
    extracted_data['name'] = extracted_data['name'].apply(lambda x: base64.b64encode(x.encode()).decode())

# Convert the 'date' column to Unix timestamp
if 'date' in extracted_data.columns:
    extracted_data['date'] = pd.to_datetime(extracted_data['date']).apply(lambda x: int(x.timestamp()))

# Write the extracted data to the csv_store.csv file
extracted_data.to_csv(csv_store_path, index=False)

# Write the extracted data to an Excel file

# Store the data in a userdata list
userdata = extracted_data.to_dict(orient='records')
for i in userdata:
    print(i)

print(f'Extracted data has been written to {csv_store_path} and {excel_store_path}')