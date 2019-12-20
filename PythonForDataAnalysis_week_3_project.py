#!/usr/bin/env python
# coding: utf-8

# # Introduction To Python For Data Analysis Week 3 Homework

# ## Instructions
# In the cell below please complete the function.  The function takes two arguments.  The first argument is a the names dataframe that we have used in class, the second argument is _name_.  The function should return a new dataframe that only contains the rows where the 'Name' column equals the _name_ argument.
# 
# You normally would not wrap this code inside a function - it is too simple to put inside a function, but putting the code inside a functions assists the grader.

# In[ ]:


def returnDataForOneName(namesDF, name):
    '''
    Please return from this function the rows from namesDF where the 'Name'
    column is equal to the name argument that is passed to this function.
    
    '''
    newDF = namesDF.loc[namesDF['Name'] == name, :]
    return newDF


# ## Test your function in the cell below:

# In[ ]:


import pandas as pd
name_data_path = '' # change this to the path of the name data file on your computer
# Now load the data:
nameDF = pd.read_csv(name_data_path) 
newDF = returnDataForOneName(nameDF, 'Michael')

# Now use some of the methods we have used to explore dataframes (like .head)
# to see if newDF only contains rows where "Name" equals 'Michael'. Then 
# change the name you are passing to the function and try again - this function
# must work for other names, not just 'Michael'.


# In[ ]:




