#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


cars = pd.read_csv('cars.csv')
cars


# In[3]:


cars.iloc[0:5, 1:10:2]


# In[4]:


cars.iloc[1]


# In[5]:


cars.iloc[23,2]


# In[79]:


Models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(Models), ['Model', 'cyl', 'gear']]


# In[ ]:




