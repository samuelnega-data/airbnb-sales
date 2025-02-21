# Airbnb Dataset Analysis 

## Overview
I conducted an in-depth analysis of Airbnb data, exploring various columns such as neighborhoods, prices, room types, and bed configurations. Using Python, I not only performed the analysis but also created insightful visualizations utilizing Seaborn and Matplotlib. Through this comprehensive examination, I uncovered several key insights, which I have presented in detail.

## Importing libraries  
I imported the necessary libraries, including pandas, seaborn, numpy, and matplotlib, to facilitate data analysis and visualization.
```pyt
import pandas as pd 
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
```
## Exploring Datasets 
These script offers a quick overview of the dataset, including its size, structure, summary statistics, and missing values, helping in the initial exploration and understanding of the data.```pyt
df.tail(2)
df.shape
df.info()
df.describe()
df.isnull().sum()
```
## Transforming DataSet 
These script checks for and removes duplicate rows, then verifies the changes by displaying the first two rows. It helps clean the dataset, ensuring the analysis uses only unique entries.
```pyt
df.duplicated().sum()
df.drop_duplicates(inplace=True)
df.duplicated().sum()
df.head(2)
```
## EDA - Univariate Analysis
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
## EDA - Bivariate Analysis
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
## Take Aways

## Price Distribution
This is the adjusted price distribution after removing 0.1% of the dataset, which included duplicates and outliers, resulting in a more refined price distribution.
![Price Distribution](https://github.com/samuelnega-data/airbnb/blob/main/Air%20Bnb%20Data%20Visualization/Screenshot%202025-02-20%20204128.png?raw=true)

## Reviews Distribution
This is the adjusted number of reviews distribution after removing 0.1% of the dataset, which included duplicates and outliers, resulting in a more refined price distribution.
![Reviews Distribution](https://github.com/samuelnega-data/airbnb/blob/main/Air%20Bnb%20Data%20Visualization/Screenshot%202025-02-20%20204224.png?raw=true) 

## Average Price Based on Neighbourhood and Room Type
The top-performing cities in terms of Airbnb prices are Brooklyn and Manhattan, while the lowest-performing cities are the Bronx and Staten Island. The second includes the room type along with the neighbourhood for a more indepth analysis.
![Average Price Based on Neighbourhood](https://github.com/samuelnega-data/airbnb/blob/main/Air%20Bnb%20Data%20Visualization/Screenshot%202025-02-20%20204310.png?raw=true)
![Average Price Based on Neighbourhood and Room Type](https://github.com/samuelnega-data/airbnb/blob/main/Air%20Bnb%20Data%20Visualization/Screenshot%202025-02-20%20204342.png?raw=true
)

## Scatter Plot
The scatter plot below shows the average price of Airbnb listings based on reviews and neighborhood groups. It reveals that Manhattan receives the highest number of reviews but is priced lower compared to other neighborhoods. Interestingly, some Manhattan listings with fewer reviews are priced much higher. This could be valuable insight for new Airbnb hosts, suggesting they may want to focus on properties in Manhattan.
![Scatter Plot](https://github.com/samuelnega-data/airbnb/blob/main/Air%20Bnb%20Data%20Visualization/Screenshot%202025-02-20%20204357.png?raw=true)

![Scatter Plot](https://github.com/samuelnega-data/airbnb/blob/main/Air%20Bnb%20Data%20Visualization/Screenshot%202025-02-20%20204419.png?raw=true)

## Room Distribution Based on Geographical Location
I used latitude and longitude to visualize the distribution of room types based on location. The analysis shows that most Airbnbs are concentrated in Manhattan and Brooklyn. Notably, Airbnbs in Manhattan generate the highest revenue. From an investment perspective, someone looking to own Airbnbs should consider focusing on properties in these two areas.
![Scatter Plot Map](https://github.com/samuelnega-data/airbnb/blob/main/Air%20Bnb%20Data%20Visualization/Screenshot%202025-02-20%20204502.png?raw=true)
