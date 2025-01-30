import pandas as pd  # Library for data manipulation
import numpy as np  # Library for numerical operations
import seaborn as sns  # Library for data visualization
import matplotlib.pyplot as plt  # Library for plotting graphs
from sklearn.preprocessing import LabelEncoder  # Library for encoding categorical variables

from sklearn.preprocessing import StandardScaler

# Load the Titanic dataset from Seaborn
titanic = sns.load_dataset('titanic')

# Step 1: Handle Categorical Variables
# Convert 'sex' and 'embarked' into numerical labels using LabelEncoder
label_encoder = LabelEncoder()
titanic['sex'] = label_encoder.fit_transform(titanic['sex'])  # Encode 'sex' (male:1, female:0)
titanic['embarked'] = label_encoder.fit_transform(titanic['embarked'])  # Encode 'embarked' (C, Q, S into numbers)

# Convert 'who' into binary (man: 1, woman: 0)
titanic['who'] = titanic['who'].apply(lambda x: 1 if x == 'man' else 0)

# Step 2: Feature Engineering
# Create a new feature 'family_size' which is the sum of 'sibsp' (siblings/spouses aboard) and 'parch' (parents/children aboard) plus one (self)
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1

# Step 3: Remove Duplicates
# Remove duplicate rows to ensure unique data
titanic_cleaned = titanic.drop_duplicates()

# Step 4: Handle Outliers
# Inspecting outliers in the 'fare' column using a box plot
plt.figure(figsize=(8, 4))  # Set figure size
plt.boxplot(titanic_cleaned['fare'])  # Create a box plot for 'fare' column
plt.title("Box plot for Fare (outliers detection)")  # Set title for visualization
plt.show()  # Display the plot

# Cap outliers in 'fare' to the 99th percentile
fare_cap = titanic_cleaned['fare'].quantile(0.99)
titanic_cleaned['fare'] = np.where(titanic_cleaned['fare'] > fare_cap, fare_cap, titanic_cleaned['fare'])
print("\nFare column statistics after handling outliers:")
print(titanic_cleaned['fare'].describe())

# Step 5: Normalize Numerical Data
# Normalize 'age' and 'fare' using StandardScaler
scaler = StandardScaler()
titanic_cleaned[['age', 'fare']] = scaler.fit_transform(titanic_cleaned[['age', 'fare']])
print("\nFirst 5 rows of the cleaned and wrangled data:")
print(titanic_cleaned.head())

# Step 6: Save the cleaned data to a CSV file
titanic_cleaned.to_csv('titanic_cleaned.csv', index=False)
print("\nCleaned dataset saved to 'titanic_cleaned.csv'")
