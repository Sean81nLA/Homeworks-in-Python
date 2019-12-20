#!/usr/bin/env python
# coding: utf-8

# # Assignment 4 
# 
# You will need to change the variable `labor_data_path` rto the path of the LaborSheetData.csv on your computer if you want to run this notebook.

# In[1]:


import pandas as pd


# In[4]:


# you will need to change the path to a location on your computer if you want to run this notebook
labor_data_path = 'data/LaborSheetData.csv'
labor_df = pd.read_csv(labor_data_path)


# In[5]:


labor_df.head()


# # Problem 1
# 
# Use the labor sheet data to find which manager has the most sales (sum all the sales for each manager).  In the lecture, we saw how we can use .sort_values() to sort values from low to high.  For this problem you will likely want to sort values from high to low, you can do that with .sort_values(ascending=False)

# In[7]:


manager_groups = labor_df.groupby('Manager')


# In[13]:


sum_sales_per_manager = manager_groups['Sales'].sum()
sum_sales_per_manager.sort_values(ascending=False).head()


# # Problem 2
# 
# Which manager has the highest mean sales?

# In[14]:


sum_sales_per_manager = manager_groups['Sales'].mean()
sum_sales_per_manager.sort_values(ascending=False).head()


# # Problem 3
# 
# Get the data for just the store 10606 and then answer this question: which manager has the highest mean sales for store 10606?
# 

# In[18]:


store_10606 = labor_df.loc[labor_df["Store"] == 10606]
store_10606_manager_groups = store_10606.groupby("Manager")
store_10606_manager_groups['Sales'].mean().sort_values(ascending=False).head()


# # Problem 4
# Which manager has managed the fewest hours at store 10606?
# 
# There is one row per hour, so we can just look at the number of rows in each manager group.

# In[22]:


store_10606_manager_groups.size().sort_values().head()


# # Problem 5
# 
# Create a new column in labor sheet dataframe (no longer just filtered on store 10606, but the entire dataframe) called 'Sales +/-' which equals the 'Sales' column minus the 'Project Sales' column. This column indicates how many sales they made above, or below, the projected sales.Which manager has the greatest mean 'Sales +/-' value?

# In[28]:


labor_df["Sales +/-"] = labor_df["Sales"] - labor_df["Projected Sales"]
# We do not need to recrate the managers groups object because we have not reordered or
# added rows to the original dataframe
manager_groups['Sales +/-'].mean().sort_values(ascending=False).head()


# In[ ]:




