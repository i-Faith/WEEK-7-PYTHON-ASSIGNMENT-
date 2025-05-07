# Iris Dataset Analysis Project - (PLP)

This project demonstrates data analysis and visualization using the Iris flower dataset. The goal is to clean the data, perform descriptive analysis, and visualize key insights using Python's data science libraries.

## 📁 Dataset

The dataset used is the **Iris.csv** file, which includes measurements of sepal and petal length and width for three species of Iris flowers: *Setosa*, *Versicolor*, and *Virginica*.

###Columns:
- `SepalLengthCm`
- `SepalWidthCm`
- `PetalLengthCm`
- `PetalWidthCm`
- `Species`

## Project Tasks

### ✅ Task One: Data Loading and Cleaning
- Loaded the dataset using pandas with error handling.
- Displayed the first few rows and data types.
- Checked for missing values.
- Cleaned the data by:
  - Filling missing numeric values with column means.
  - Dropping any rows with remaining missing values.

### ✅ Task Two: Data Analysis
- Generated descriptive statistics using `.describe()` and `.median()`.
- Grouped data by `Species` to calculate mean measurements.
- Key observations:
  - *Setosa* has the smallest petal size.
  - *Virginica* generally has the largest sepal and petal measurements.

### ✅ Task Three: Data Visualization
- **Line Chart**: Simulated monthly average sepal lengths (dummy data).
- **Bar Chart**: Compared average petal length by species.
- **Histogram**: Displayed distribution of sepal width.
- **Scatter Plot**: Showed relationship between sepal and petal length across species.

## 🛠 Technologies Used

- **Python**
- **Pandas** – for data handling and analysis
- **Matplotlib** – for plotting charts
- **Seaborn** – for advanced visualizations
- **NumPy** – for numerical operations

## 📦 How to Run

1. Make sure Python and necessary libraries are installed:
   pip install pandas
   pip install matplotlib
   pip install seaborn
   pip install numpy 

2. Save the dataset (`Iris.csv`) in your desired working directory.

3. Run the Python script:
python data_analysis.py
  
## 📈 Example Visuals

- Line chart of average sepal length over months
- Bar chart comparing petal lengths across species
- Histogram of sepal width distribution
- Scatter plot of sepal vs. petal length colored by species

## Author

Cheptoo Faith  
Python & Data Analysis Learner

## 📄 License

This project is for learning purposes and not intended for commercial use. 
Dataset used is publicly available under the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris).
