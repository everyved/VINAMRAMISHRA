import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('tips2.csv')
print(df.head())

# 1)Univariate analysis
plt.figure(figsize=(10, 6))
sns.histplot(df['bill'], kde=True, color='red')
plt.title('Distribution of Bill Amounts')
plt.xlabel('Bill')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x=df['bill'], color='pink')
plt.title('Boxplot of Bill Amounts')
plt.xlabel('Bill')
plt.show()

# 2) Bivarirate analysis
plt.figure(figsize=(5, 5))
sns.scatterplot(x=df['bill'], y=df['tip'], hue=df['smoker'])
plt.title('Bill vs Tip (Smoker)')
plt.xlabel('Bill')
plt.ylabel('Tip')
plt.show()


plt.figure(figsize=(5, 5))
sns.boxplot(x=df['gender'], y=df['bill'])
plt.title('Gender vs Bill Amount')
plt.xlabel('Gender')
plt.ylabel('Bill')
plt.show()

# multivariate analysis
plt.figure(figsize=(5, 5))
sns.heatmap(df[['bill', 'tip', 'size']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

sns.pairplot(df, hue='gender')
plt.title('Pairplot for Gender and Other Variables')
plt.show()
