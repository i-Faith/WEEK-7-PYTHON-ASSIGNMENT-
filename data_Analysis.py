#TASK ONE
import pandas as pd
#Loading the data with error handling
try:
   df = pd.read_csv(r"c:\Users\Admin\Desktop\PLP\python lessons\WEEK 7 ASSIGNMENT\Iris.csv")
   print("✅ Data loaded successfully.")
except FileNotFoundError:
    print("❌ Error: File not found.")
except pd.errors.EmptyDataError:
    print("❌ Error: File is empty.")

#Displaying the first few rows of the dataset
print(df.head())
#Checking the datatypes
print(df.dtypes)

#Checking for missing values
print(df.isnull().sum())

#Cleaning the dataset 
# filling mising values
df_cleaned = df.fillna(df.mean(numeric_only=True))
# dropping any missing values.
df_cleaned = df.dropna()



#TASK TWO
# Descriptive statistics
df.describe()
print(df.describe())
# Medianload 
df.median(numeric_only=True)
print (df.median)

# Group by type of cancer and compute mean of numeric columns
grouped_means = df.groupby('Species').mean(numeric_only=True)
print(grouped_means)
# Observation
print("Observations:")
print("- Setosa has the smallest petal length and width.")
print("- Virginica species generally has the largest sepal and petal measurements.")



#TASK THREE
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#Showing the list of columns
print(df.columns)

#Line Chart
# Simulate monthly average sepal lengths (fake data)
months = pd.date_range(start="2024-01-01", periods=6, freq='M')
avg_sepal_lengths = [5.0, 5.1, 5.3, 5.2, 5.4, 5.3]

plt.figure(figsize=(8,5))
plt.plot(months, avg_sepal_lengths, marker='o', linestyle='-')
plt.title("Average Sepal Length Over 6 Months")
plt.xlabel("Month")
plt.ylabel("Average Sepal Length (cm)")
plt.grid(True)
plt.tight_layout()
plt.show()

#Bar Chart – Comparison Across Categories
#Comparing average petal length for each species.
plt.figure(figsize=(8,5))
sns.barplot(x="Species", y="PetalLengthCm", data=df, estimator=np.mean)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.tight_layout()
plt.show()


#Histogram – Distribution of a Numerical Column
#Distribution of sepal width.
plt.figure(figsize=(8,5))
plt.hist(df['SepalWidthCm'], bins=15, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


#Scatter Plot – Relationship Between Two Numerical Columns
#Relationship between sepal length and petal length.
plt.figure(figsize=(8,5))
sns.scatterplot(x="SepalLengthCm", y="PetalLengthCm", hue="Species", data=df)
plt.title("Sepal Length vs. Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()





