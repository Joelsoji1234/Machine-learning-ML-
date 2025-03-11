import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'F:\SEM 6\Machine Learning\Dataset\ev_charging_patterns.csv'  # Replace with your dataset path
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Select numerical columns
num_cols = df.select_dtypes(include=['float64', 'int64']).columns

# ------ Univariate Analysis ------
def univariate_analysis(data):
    for column in data.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(data[column], kde=True, bins=20, color='blue', edgecolor='black')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

# ------ Bivariate Analysis ------
def bivariate_analysis(data):
    num_cols = data.select_dtypes(include=['float64', 'int64']).columns
    for col1 in num_cols:
        for col2 in num_cols:
            if col1 != col2:
                plt.figure(figsize=(8, 5))
                sns.scatterplot(x=data[col1], y=data[col2], alpha=0.7)
                plt.title(f'{col1} vs {col2}')
                plt.xlabel(col1)
                plt.ylabel(col2)
                plt.show()

# ------ Multivariate Analysis ------
def multivariate_analysis(data):
    plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)
    plt.title('Correlation Heatmap')
    plt.show()

# ------ Execute Analysis ------
# Univariate Analysis
print("Performing Univariate Analysis...")
univariate_analysis(df[num_cols])

# Bivariate Analysis
print("Performing Bivariate Analysis...")
bivariate_analysis(df)

# Multivariate Analysis
print("Performing Multivariate Analysis...")
multivariate_analysis(df)
