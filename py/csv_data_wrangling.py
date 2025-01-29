import pandas as pd

# Load dataset (Change file path as needed)
file_path = "data.csv"  # Replace with your file path
df = pd.read_csv(file_path)  # Use pd.read_excel(file_path) for Excel files

# Display first 5 rows
print("Original Dataset:")
print(df.head())

# # Handling Missing Values
df.fillna(value={"ColumnName": df["ColumnName"].mean()}, inplace=True)  # Replace missing values in a column
# print(df.head())
#
# # Filter Data (Example: Select rows where "Age" > 25)
filtered_df = df[df["Age"] > 25]
print('\n')
# print(filtered_df)
#
# # Modify Data (Create new column based on existing data)
df["Salary_in_Lakhs"] = df["Salary"] / 100000  # Converting salary to lakhs
print('\n',df.head())
#
# # Sorting Data
sorted_df = df.sort_values(by="Salary", ascending=False)
print('\n',sorted_df)
#
# # Grouping Data (Example: Group by "Department" and get mean salary)
grouped_df = df.groupby("Department")["Salary"].mean().reset_index()
print('\n',grouped_df)
#
# # Export cleaned data
df.to_csv("cleaned_data.csv", index=False)
