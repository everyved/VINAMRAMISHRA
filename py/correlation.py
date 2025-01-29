import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'car.csv'
df = pd.read_csv(file_path)

numerical_features = [
    'wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight',
    'enginesize', 'boreratio', 'stroke', 'compressionratio',
    'horsepower', 'peakrpm', 'citympg', 'highwaympg', 'price'
]
numerical_df = df[numerical_features]

correlation_matrix = numerical_df.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap: Car Dataset')
plt.show()
