#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


cars = pd.read_csv('cars.csv')


# In[26]:


cars.iloc[:5, 1::2]


# In[23]:


cars.loc[cars['Model']=='Mazda RX4']


# In[24]:


cars.loc[cars['Model']=='Camaro Z28', ['cyl']]


# In[25]:


cars_models = ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(cars_models), ['cyl', 'gear']]

