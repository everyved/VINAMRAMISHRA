import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


boston_df = pd.read_csv('Boston.csv')
print(boston_df.head())
print(boston_df.describe())
boston_df = boston_df.drop(columns=['Unnamed: 0'])
print(boston_df.head())

# numeric dataframe
num_df = boston_df.select_dtypes(include='number')

print(num_df.head())

num_df['crim'].skew()

# KDEPLOT to show shape
sns.kdeplot(x='crim',data=num_df)
plt.title('Shape of crim column to indicate distribution')
plt.show()

print(num_df['crim'].kurtosis())

# Histogram
plt.figure(figsize=(5,5))
sns.histplot(x='crim',data=num_df)
plt.show()

# check outliers
crim_summary = num_df['crim'].describe()
q1 = crim_summary[4]
print(q1)

q2 = crim_summary[5]
print(q2)

q3 = crim_summary[6]
print(q3)

# calculate the quartiles manually
quartile1 = np.quantile(num_df['crim'],.25)
quartile2 = np.quantile(num_df['crim'],.50)
quartile3 = np.quantile(num_df['crim'],.75)

print(quartile3,quartile2,quartile1)

# calculate IQR
iqr = q3 - q1
print(iqr)
# calculate range
ub = q3 + (1.5 * iqr)
lb = q1 - (1.5 * iqr)

# print the outliers
print(num_df[(num_df.crim<lb) | (num_df.crim>ub)])

print(len(num_df[(num_df.crim<lb) | (num_df.crim>ub)]))

sns.boxplot(num_df['crim'])
plt.show()

df_wo_crim = num_df[(num_df.crim>=lb)&(num_df.crim<=ub)]
print(df_wo_crim)

sns.boxplot(x=df_wo_crim.crim,data=df_wo_crim)
plt.show()

cap = np.quantile(num_df['crim'],.95)
print(cap)

num_df.loc[num_df.crim > ub,'crim'] = cap
print(num_df)

print(num_df[num_df.crim > ub])

# analysis zone column
sns.kdeplot(x=num_df['zn'],data=num_df)
plt.show()

print(num_df['zn'].skew())

print(num_df['zn'].kurtosis())

sns.histplot(x='zn',data=num_df)
plt.show()

print(num_df.zn.describe())

print(num_df.zn.value_counts())

print(num_df.zn.mode())

# countplot to visualize the frequency table
plt.figure(figsize=(5,5))
sns.countplot(x='zn',data=num_df,color='green')
plt.show()

# Outlier Analysis
q1_zn = np.quantile(num_df.zn,.25)
q3_zn = np.quantile(num_df.zn,.75)
iqr_zn = q3_zn - q1_zn

lb_zn = q1_zn = (1.5 * iqr)
ub_zn = q3_zn + (1.5 * iqr_zn)

print(lb_zn,ub_zn)

print(num_df[(num_df.zn < lb)|(num_df.zn > ub)])

sns.boxplot(x='zn',data=num_df)
plt.show()

