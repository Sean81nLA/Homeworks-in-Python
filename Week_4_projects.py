#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem 1

def raise_to_power(x):
    '''Return a function that raises the argument to nth power'''
    def power_raise_func(n):
        '''Raise to nth power'''
        return x**n
    return power_raise_func


# In[ ]:


# Problem 2

def file_writer(filepath):
    '''Return the function that will write the string to the file specified in the file path'''
    def write_to_file(filepath_a):
      '''Open filepath in append mode'''  
        with open(filepath, 'a') as write_to_file:
            '''write the string to the file in filepath'''
           write_to_file.write(filepath_a)
    return write_to_file


# In[ ]:


# Problem 3

def word_n_each_line(n):
    '''Define function that returns n words from the line'''
    def word_of_each_line(filepath_n):
       """Generate first words from the file, line by line"""
    # First, open the file
    with open(filepath_n, 'r') as my_file:
        # Loop through the lines
        for line in my_file:
            line = line.strip() # strip whitespace from the line
            word = line.split()
            yield word[n] if len(word)>n else None

