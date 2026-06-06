Iris Dataset Exploratory Data Analysis (EDA) and Data Visualization

Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) and Data Visualization on the given Datasets using Python. The objective is to understand the structure of the dataset, identify patterns, summarize key statistics, and visualize relationships between variables.

 Objectives

* Clean and prepare the dataset for analysis.
* Generate descriptive statistics.
* Explore relationships among features.
* Visualize feature distributions and species comparisons.
* Gain insights from the dataset through graphical analysis.

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

## Data Cleaning

The following preprocessing steps were performed:

* Removed missing values using `dropna()`
* Removed duplicate records using `drop_duplicates()`
* Verified data integrity before visualization

## Exploratory Data Analysis

The following statistical analyses were conducted:

* Mean
* Median
* Standard Deviation
* Data distribution analysis
* Species-based feature comparison

## Data Visualizations

### Bar Charts

Bar plots were used to compare average measurements across different iris species:

* Mean Sepal Length by Species
* Mean Sepal Width by Species
* Mean Petal Length by Species
* Mean Petal Width by Species

### Scatter Plots

Scatter plots were used to examine relationships between features and identify clustering among species:

* Sepal Length vs Sepal Width
* Petal Length vs Petal Width

### Subplots

Related visualizations were grouped using Matplotlib subplots to improve readability and comparison.

## Key Insights

* Petal measurements provide clearer separation between species than sepal measurements.
* Iris Setosa is distinctly different from the other species in petal dimensions.
* Iris Versicolor and Iris Virginica exhibit some overlap but remain distinguishable through petal features.
* No significant missing or duplicate records remained after cleaning.

## Challenges Encountered

* Managing multiple visualizations without overlap.
* Choosing suitable plot types for categorical and numerical variables.
* Organizing related charts using subplots.
* Properly labeling plots with titles, legends, and axis labels.
* Understanding aggregation functions and summary statistics.


## How to Run

1. Clone the repository.

2. Install dependencies.

3. Run the analysis script.

## Learning Outcomes

Through this project, I gained practical experience in:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Statistical summarization
* Data visualization using Seaborn and Matplotlib
* Creating professional and interpretable visualizations
* Organizing multiple plots using subplots

## Author

Tumi Akintola

Computer Engineering Student | Data Scientist | Aspiring Chip Designer
