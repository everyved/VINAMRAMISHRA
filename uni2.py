import pandas as pd  # Importing Pandas for data manipulation
import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for visualization
import seaborn as sns  # Importing Seaborn for enhanced visualizations

# Load the Boston dataset
boston_df = pd.read_csv('Boston.csv')
print(boston_df.head())  # Display first few rows of the dataset
print(boston_df.describe())  # Summary statistics of the dataset

# Drop the 'Unnamed: 0' column which appears to be an unnecessary index column
boston_df = boston_df.drop(columns=['Unnamed: 0'])
print(boston_df.head())  # Display dataset after dropping the column

# Select only numeric columns from the dataset
num_df = boston_df.select_dtypes(include='number')
print(num_df.head())  # Display first few rows of numeric columns

# Compute skewness of the 'crim' column
print(num_df['crim'].skew())

# Kernel Density Estimation (KDE) plot to visualize the distribution of 'crim'
sns.kdeplot(x='crim', data=num_df)
plt.title('Shape of crim column to indicate distribution')
plt.show()

# Compute kurtosis of the 'crim' column
print(num_df['crim'].kurtosis())

# Histogram for 'crim' column
plt.figure(figsize=(5,5))
sns.histplot(x='crim', data=num_df)
plt.show()

# Checking outliers in 'crim' column
crim_summary = num_df['crim'].describe()
q1 = crim_summary[4]  # First quartile (25th percentile)
print(q1)
q2 = crim_summary[5]  # Median (50th percentile)
print(q2)
q3 = crim_summary[6]  # Third quartile (75th percentile)
print(q3)

# Manually calculating quartiles
quartile1 = np.quantile(num_df['crim'], .25)
quartile2 = np.quantile(num_df['crim'], .50)
quartile3 = np.quantile(num_df['crim'], .75)
print(quartile3, quartile2, quartile1)

# Interquartile Range (IQR) calculation
iqr = q3 - q1  # IQR = Q3 - Q1
print(iqr)

# Calculating upper and lower bounds for outliers
ub = q3 + (1.5 * iqr)  # Upper bound
lb = q1 - (1.5 * iqr)  # Lower bound

# Identifying and printing outliers
print(num_df[(num_df.crim < lb) | (num_df.crim > ub)])
print(len(num_df[(num_df.crim < lb) | (num_df.crim > ub)]))

# Boxplot to visualize outliers in 'crim'
sns.boxplot(num_df['crim'])
plt.show()

# Removing outliers from 'crim'
df_wo_crim = num_df[(num_df.crim >= lb) & (num_df.crim <= ub)]
print(df_wo_crim)

# Boxplot of cleaned 'crim' column
sns.boxplot(x=df_wo_crim.crim, data=df_wo_crim)
plt.show()

# Capping outliers in 'crim' at the 95th percentile
cap = np.quantile(num_df['crim'], .95)
print(cap)
num_df.loc[num_df.crim > ub, 'crim'] = cap
print(num_df)
print(num_df[num_df.crim > ub])  # Check if any outliers remain

# Analysis of 'zn' column
sns.kdeplot(x=num_df['zn'], data=num_df)
plt.show()

# Compute skewness and kurtosis of 'zn' column
print(num_df['zn'].skew())
print(num_df['zn'].kurtosis())

# Histogram for 'zn'
sns.histplot(x='zn', data=num_df)
plt.show()

# Summary statistics of 'zn'
print(num_df.zn.describe())

# Count unique values in 'zn'
print(num_df.zn.value_counts())
print(num_df.zn.mode())  # Find the most frequently occurring value

# Countplot to visualize frequency distribution
plt.figure(figsize=(5,5))
sns.countplot(x='zn', data=num_df, color='green')
plt.show()

# Outlier analysis for 'zn'
q1_zn = np.quantile(num_df.zn, .25)  # First quartile
q3_zn = np.quantile(num_df.zn, .75)  # Third quartile
iqr_zn = q3_zn - q1_zn  # IQR calculation

# Calculating upper and lower bounds for outliers in 'zn'
lb_zn = q1_zn - (1.5 * iqr_zn)  # Lower bound
ub_zn = q3_zn + (1.5 * iqr_zn)  # Upper bound
print(lb_zn, ub_zn)

# Identifying outliers in 'zn'
print(num_df[(num_df.zn < lb_zn) | (num_df.zn > ub_zn)])

# Boxplot for 'zn' to visualize outliers
sns.boxplot(x='zn', data=num_df)
plt.show()
