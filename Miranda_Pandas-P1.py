#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Import pandas
import pandas as pd


# In[2]:

# import csv file to the program
cars = pd.read_csv('cars.csv')
cars


# In[3]:

# Display the first five rows
cars.head(5)


# In[4]:

# Display the last five rows
cars.tail(5)


# In[ ]:




