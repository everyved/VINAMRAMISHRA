import pandas as pd

# Step 1: Create Sample Data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 2: Save Data in Text Format
text_file_path = "data.txt"
df.to_csv(text_file_path, index=False, sep='\t')  # Using tab-delimiter for text format
print(f"Data saved in text format at: {text_file_path}")

# Step 3: Read Data Back from the Text File
read_df = pd.read_csv(text_file_path, sep='\t')
print("Data read from the text file:")
print(read_df)

# Step 4: Save and Read in Other Formats

# Save as JSON
json_file_path = "data.json"
df.to_json(json_file_path, orient='records', lines=True)
print(f"Data saved in JSON format at: {json_file_path}")

# Read JSON file
read_json_df = pd.read_json(json_file_path, orient='records', lines=True)
print("Data read from JSON file:")
print(read_json_df)


# Step 1: Create a More Complex Dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, None],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Salary": [70000, 80000, 120000, 110000, None],
    "Department": ["HR", "Finance", "Engineering", "Management", "HR"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 2: Data Cleaning
# Handle missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

# Add a new calculated column
df["Tax"] = df["Salary"] * 0.2

# Step 3: Save Data in Multiple Formats

# Save as CSV
csv_file_path = "complex_data.csv"
df.to_csv(csv_file_path, index=False)
print(f"Data saved as CSV at: {csv_file_path}")

# Save as JSON
json_file_path = "complex_data.json"
df.to_json(json_file_path, orient='records', lines=True)
print(f"Data saved as JSON at: {json_file_path}")

# Read JSON file
read_json_df = pd.read_json(json_file_path, orient='records', lines=True)
print("Data read from JSON file:")
print(read_json_df)

# Step 4: Read Data Back and Perform Analysis
# Read from CSV
read_csv_df = pd.read_csv(csv_file_path)
print("Data read from CSV:")
print(read_csv_df)

# Read from JSON
read_json_df = pd.read_json(json_file_path, orient='records', lines=True)
print("Data read from JSON:")
print(read_json_df)

# Step 5: Advanced Analysis
# Group by Department and Calculate Mean Salary
grouped_df = df.groupby("Department")["Salary"].mean().reset_index()
print("Average Salary by Department:")
print(grouped_df)

# Save Grouped Data as Excel
excel_file_path = "grouped_data.xlsx"
grouped_df.to_excel(excel_file_path, index=False)
print(f"Grouped data saved as Excel at: {excel_file_path}")
