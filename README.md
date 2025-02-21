# Airbnb Dataset Analysis 

## Overview
I conducted an in-depth analysis of Airbnb data, exploring various columns such as neighborhoods, prices, room types, and bed configurations. Using Python, I not only performed the analysis but also created insightful visualizations utilizing Seaborn and Matplotlib. Through this comprehensive examination, I uncovered several key insights, which I have presented in detail.

### Importing libraries  
I imported the necessary libraries, including pandas, seaborn, numpy, and matplotlib, to facilitate data analysis and visualization.
```pyt
import pandas as pd 
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
```
### Exploring Datasets 
These script offers a quick overview of the dataset, including its size, structure, summary statistics, and missing values, helping in the initial exploration and understanding of the data.```pyt
df.tail(2)
df.shape
df.info()
df.describe()
df.isnull().sum()
```
### Transforming DataSet 
These script checks for and removes duplicate rows, then verifies the changes by displaying the first two rows. It helps clean the dataset, ensuring the analysis uses only unique entries.
```pyt
df.duplicated().sum()
df.drop_duplicates(inplace=True)
df.duplicated().sum()
df.head(2)
```
### EDA - Univariate Analysis
This analysis explores the 'price' and 'number_of_reviews' features, filtering extreme values and visualizing their distributions. It also calculates the average price and price per bed by neighborhood group, helping to identify patterns and outliers.
```pyt
sb.boxplot(data=df, x='price')
dff = df[df['price'] < 1500]
print(dff)
sb.histplot(data=dff, x='price')
plt.title('Price Distribution')
sns.boxplot(data=dff, x='price')
sb.boxplot(data=dff, x='price')
sb.histplot(data=dff, x='price')
plt.ylabel('Frequency')
plt.title('Price Distribution')
dff.columns
sb.boxplot(data=dff, x='number_of_reviews')
sb.boxplot(data=dff, x='number_of_reviews_ltm')
dfn = df[df['number_of_reviews_ltm'] < 100]
print(dff)
sb.histplot(data=dfn, x='number_of_reviews_ltm')
dff.head(4)
dff.groupby('neighbourhood_group')['price'].mean()
dff.info()
dff['price per bed']=dff['price']/dff['beds']
dff.head()
dff.groupby('neighbourhood_group')['price per bed'].mean()
dff.columns
sb.barplot(data=dff, x='neighbourhood_group', y='price')
```
### EDA - Bivariate Analysis
In this bivariate analysis, you examine relationships between variables like price, room type, neighborhood, and reviews using bar plots, scatter plots, and pair plots. You also explore geographical distributions by latitude and longitude and analyze correlations between key variables with a heatmap. This helps uncover patterns and relationships within the data for deeper insights.
```pyt
sb.barplot(data=dff, x='neighbourhood_group', y='price', hue='room_type')
sb.scatterplot (data=dff, x='number_of_reviews', y='price', hue='neighbourhood_group')
plt.title('Number of Reviews vs Price vs Neighborhood')
dff.dtypes
sb.pairplot(data=dff, vars=['price', 'minimum_nights', 'number_of_reviews', 'availability_365'], hue='room_type')
sb.scatterplot(data=dff, x='latitude', y='longitude', hue='neighbourhood_group')
sb.scatterplot(data=dff, x='latitude', y='longitude', hue='room_type')
corr = dff[['latitude', 'longitude', 'price','minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365', 'price per bed']]
sb.heatmap(data=corr.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Map")
```
### Take Aways
