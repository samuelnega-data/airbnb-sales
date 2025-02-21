#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Importing all the libraries that are needed 

import pandas as pd 
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv (r"C:\Users\samue\OneDrive\Desktop\datasets.csv", encoding_errors='ignore')


# In[3]:


#2 Exploring Dataset

df.tail(2)


# df.shape

# In[4]:


df.info()

#Each of the data types column by column


# In[5]:


df.describe()

#Interesting insights specifically pretaining around the number of reviews, beds available. Also interested in looking at the lat and long values maybe visualize it. 


# In[6]:


df.isnull().sum()

#I am dropping all the rows with missing values since it will only be removing 0.5% of the rows on the higher end. I will be caclulating the exact percentage in the next code.
df.dropna(inplace=True)


# In[7]:


df.shape

#Only 34 rows have been deleted this shows the insignificance of dropping the rows this translate to a 0.1% change in the original dataset.


# In[8]:


#Checking to see if there are any duplicates.

df.duplicated().sum()


# In[9]:


#Removing Duplicated Data
df.drop_duplicates(inplace=True)


# In[10]:


df.duplicated().sum()


# In[11]:


df.head(2)


# In[12]:


#Analyzing the Data EDA (Univariate Analysis)


# In[13]:


#Identifying the outliers 

sb.boxplot(data=df, x='price')


# In[14]:


# Filters rows where 'price' is less than 1500
dff = df[df['price'] < 1500]
print(dff)


# In[17]:


#Price distribution 

sb.histplot(data=dff, x='price')
plt.title('Price Distribution')


# sns.boxplot(data=dff, x='price')

# In[18]:


#Outliers have been removed

sb.boxplot(data=dff, x='price')


# In[19]:


sb.histplot(data=dff, x='price')
plt.ylabel('Frequency')
plt.title('Price Distribution')


# In[20]:


dff.columns


# In[21]:


#Analyzing distribution across other factors 

sb.boxplot(data=dff, x='number_of_reviews')


# In[22]:


sb.boxplot(data=dff, x='number_of_reviews_ltm')


# In[23]:


dfn = df[df['number_of_reviews_ltm'] < 100]
print(dff)


# In[24]:


sb.histplot(data=dfn, x='number_of_reviews_ltm')


# In[25]:


dff.head(4)


# In[26]:


#Looking at the average price by neighbourhood group

dff.groupby('neighbourhood_group')['price'].mean()


# In[27]:


dff.info()


# In[28]:


#Adding New Column for Price per Bed 

dff['price per bed']=dff['price']/dff['beds']
dff.head()


# In[29]:


#Looking at the average price per bed for each neighboorhood group

dff.groupby('neighbourhood_group')['price per bed'].mean()


# In[30]:


#Performing Bi Variable Analysis 


# In[31]:


dff.columns


# In[32]:


#Price dependency on neighbourhood group

sb.barplot(data=dff, x='neighbourhood_group', y='price')


# In[33]:


#Price dependency on neighbourhood group and rooms

sb.barplot(data=dff, x='neighbourhood_group', y='price', hue='room_type')


# In[34]:


#Number of reviews and price

sb.scatterplot (data=dff, x='number_of_reviews', y='price', hue='neighbourhood_group')
plt.title('Number of Reviews vs Price vs Neighborhood')


# In[35]:


dff.dtypes


# In[36]:


sb.pairplot(data=dff, vars=['price', 'minimum_nights', 'number_of_reviews', 'availability_365'], hue='room_type')


# In[37]:


# Creating scatter plot using the lagitude and longetude to see geographical distribution of room types

sb.scatterplot(data=dff, x='latitude', y='longitude', hue='neighbourhood_group')


# In[38]:


sb.scatterplot(data=dff, x='latitude', y='longitude', hue='room_type')


# In[40]:


#Creating a heat map and assessing the correlation of one variable with another for numberical columns 

corr = dff[['latitude', 'longitude', 'price','minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365', 'price per bed']]
sb.heatmap(data=corr.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Map")


# In[ ]:




