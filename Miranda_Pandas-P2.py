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

# Find and display the first five rows and odd-numbered columns in the table
cars.iloc[0:5, 1:10:2]


# In[4]:

# Display the row with the 'Model' of 'Mazda RX4'
cars.iloc[1]


# In[5]:

# Number of 'cyl' Camero Z28 has.
cars.iloc[23,2]


# In[79]:

# Display the 'cyl', 'gear' and 'model' of Mazda XR4, Ford Pantera and Honda Civic
Models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(Models), ['Model', 'cyl', 'gear']]


# In[ ]:




