import pandas as pd

# ✔ Loads the dataset using pandas
# ✔ Groups data by "Department" and calculates average salary
# ✔ Sorts data by "Salary" in descending order
# ✔ Prints the results
# ✔ Exports cleaned data to new CSV files
#

# Load the dataset from CSV file
file_path = "data.csv"  # Update the path if necessary
df = pd.read_csv(file_path)

# Performing Group By operation - Average Salary per Department
grouped_df = df.groupby("Department")["Salary"].mean().reset_index()

# Sorting Data by Salary in Descending Order
sorted_df = df.sort_values(by="Salary", ascending=False)

# Display results
print("Grouped Data - Average Salary per Department:")
print(grouped_df)

print("\nSorted Data - Salary Descending:")
print(sorted_df)

# Exporting results to CSV files
grouped_df.to_csv("grouped_salary.csv", index=False)
sorted_df.to_csv("sorted_salary.csv", index=False)
