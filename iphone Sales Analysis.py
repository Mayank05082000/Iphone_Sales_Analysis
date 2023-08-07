#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data=pd.read_csv("apple_products.csv")


# In[3]:


print(data.isnull().sum())


# In[4]:


data.describe()


# # iphone sales analysis in India 

# In[5]:


highest_rating=data.sort_values(by=['Star Rating'], ascending=False)
highest_rated = highest_rating.head(10)


# In[6]:


highest_rated


# In[7]:


iphones = highest_rated['Product Name'].value_counts()


# In[8]:


iphones


# In[16]:


iphones = highest_rated['Product Name'].value_counts()
labels = iphones.index
counts = highest_rated['Number Of Ratings']
figure = px.bar(highest_rated, x=labels,  y=counts, title = 'Number of ratings of highest rated iphones')
print(figure.show())


# In[15]:


iphones = highest_rated['Product Name'].value_counts()
labels = iphones.index
counts = highest_rated['Number Of Reviews']
figure = px.bar(highest_rated, x=labels, y=counts, title = 'Number Of Reviews')
print(figure.show())


# In[14]:


figure = px.scatter(data_frame = data, x='Number Of Ratings', y='Sale Price', size = 'Discount Percentage', trendline='ols', title='Sale price vs No of rating')
print(figure.show())


# In[13]:


figure = px.scatter(data_frame = data, x = 'Number Of Ratings', y = 'Discount Percentage' , size = 'Sale Price', trendline = 'ols', title = 'Discount Percentage vs Sale Price')
print(figure.show())


# # -------------------------END-----------------------------
