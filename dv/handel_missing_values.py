import pandas as pd  # Library for data manipulation
import seaborn as sns  # Library for visualization and dataset loading
import matplotlib.pyplot as plt  # Library for plotting graphs

# Step 1: Create a Toy Dataset
data = {
    "Product": ["Laptop", "Tablet", "Smartphone", "Monitor", None],
    "Price": [1200, None, 800, 300, 150],
    "Category": ["Electronics", "Electronics", None, "Accessories", "Accessories"],
    "Description": ["High-end laptop", "Compact and versatile", "Feature-packed smartphone",
                     None, "Affordable monitor"]
}

# Create a DataFrame
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

# Step 2: Handling Missing Data
# Fill missing Product names with "Unknown"
df["Product"].fillna("Unknown", inplace=True)

# Fill missing Prices with the median price
df["Price"].fillna(df["Price"].median(), inplace=True)

# Fill missing Categories with "Miscellaneous"
df["Category"].fillna("Miscellaneous", inplace=True)

# Fill missing Descriptions with a default value
df["Description"].fillna("No description available", inplace=True)
print("\nDataset After Handling Missing Data:")
print(df)

# Step 3: String Manipulation
# Add a new column "Short Description" with the first 10 characters of the Description
df["Short Description"] = df["Description"].str[:10]

# Convert the Category column to uppercase
df["Category"] = df["Category"].str.upper()

# Replace spaces with hyphens in the Product column
df["Product"] = df["Product"].str.replace(" ", "-", regex=False)
print("\nDataset After String Manipulation:")
print(df)

# Step 4: Save the Cleaned and Transformed Dataset
cleaned_file_path = "cleaned_data.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned data saved as CSV at: {cleaned_file_path}")

# Step 5: Load and Analyze the Penguins Dataset
penguins = sns.load_dataset("penguins")
print("Original Dataset:")
print(penguins.head())

# Step 6: Exploratory Data Analysis (EDA)
print("\nDataset Info:")
print(penguins.info())

# Describe numerical columns
print("\nStatistical Summary of Numerical Columns:")
print(penguins.describe())

# Check for missing values
print("\nMissing Data:")
print(penguins.isnull().sum())

# Visualizations
plt.figure(figsize=(8, 6))
sns.histplot(penguins['bill_length_mm'], kde=True, bins=20, color="blue")
plt.title("Distribution of Bill Length")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Frequency")
plt.show()

# Boxplot for flipper length by species
plt.figure(figsize=(8, 6))
sns.boxplot(x="species", y="flipper_length_mm", data=penguins, palette="Set2")
plt.title("Flipper Length by Species")
plt.xlabel("Species")
plt.ylabel("Flipper Length (mm)")
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(penguins.select_dtypes('float64').corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Step 7: Handle Missing Data
penguins["bill_length_mm"].fillna(penguins["bill_length_mm"].mean(), inplace=True)
penguins["bill_depth_mm"].fillna(penguins["bill_depth_mm"].mean(), inplace=True)
penguins["flipper_length_mm"].fillna(penguins["flipper_length_mm"].mean(), inplace=True)
penguins["body_mass_g"].fillna(penguins["body_mass_g"].median(), inplace=True)

# Fill missing categorical values with "Unknown"
penguins["sex"].fillna("Unknown", inplace=True)
print("\nDataset After Handling Missing Data:")
print(penguins.isnull().sum())

# Step 8: String Manipulation
penguins["species_island"] = penguins["species"] + " - " + penguins["island"]
penguins["species"] = penguins["species"].str.upper()
penguins["island_code"] = penguins["island"].str[:3]
print("\nDataset After String Manipulation:")
print(penguins.head())

# Step 9: Save the Cleaned and Transformed Dataset
cleaned_file_path = "cleaned_penguins.csv"
penguins.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved as CSV at: {cleaned_file_path}")

# Step 10: Grouped Analysis
grouped_data = penguins.groupby("species")["flipper_length_mm"].mean().reset_index()
print("\nMean Flipper Length by Species:")
print(grouped_data)

# Save grouped data as Excel
grouped_file_path = "grouped_penguins.xlsx"
grouped_data.to_excel(grouped_file_path, index=False)
print(f"\nGrouped data saved as Excel at: {grouped_file_path}")
