#!/usr/bin/env python
# coding: utf-8

# # Week 2 Homework Answers:
# This notebook contains the answers to the week 2 homework. There our multiple ways to answer these problem. The answer here only use what we have learned in class. (There are other ways using techniques / functions we have not yet learned)

# ## Problem 1:
# Please complete the function, stringEvenOrOdd(inputString), that takes a string as input and returns ‘even’ or ‘odd’ (note the lower case) depending on if the string length is even or odd.

# In[1]:


def stringEvenOrOdd(inputString):
    if len(inputString) % 2 == 0:
        return 'even'
    else:
        return 'odd'
    # your code goes here
    # be sure to include a 'return' statement at the end of the function.
    # note that this cell will return an error if you run it now, without
    # completing your function.


# In[2]:


# test the function here:
result = stringEvenOrOdd('apple')
print(result)


# ## Problem 2:
# In the cell below, please define the a function, lowerList(inputList). This function takes in a list of strings and outputs the same list, but with all chaaracters lowercase.  If you input ['Apple', 'BITE'], the function will return ['apple', 'bite']. You are allowed to use the .lower() method to complete this function.

# In[ ]:


# First test the lower method here so that you can see what it does:
myString = 'ApPLe'
myStringLower = myString.lower()
print(myStringLower)


# In[3]:


# Now, define your function in this cell. Remember to start with the 'def'
# keyword, just like you did in problem 1.
def lowerList(stringList):
    newList = []
    for item in stringList:
        newList.append(item.lower())
    return newList


# In[4]:


# Test your function here:
result = lowerList(['SUSIE', 'BoB'])
print(result)


# # Problem 3:
# Please define a function called wordCount(inputString). This function takes in a string and returns a dictionary that has keys for each unique word in the string. The corresponding values are the counts of each word.
# 
# For example, if the string ‘I like small dogs and big dogs’ is passed to the function, it will return the dict, **{I:1, like:1, small:1, dogs:2, and:1, big:1}**.
# 
# Hints: You just need to be able to:
# * Convert a string to a list of words. You can use the split method to do so. For example, try the following code in your console to see an example "I like dogs".split(" ").  This code will split the string anywhere there is a " " (a space between the words)). It will create a list of the words.
# 
# * Loop through the list (we saw this in the for loop lecture)
# 
# * Add a key and value to a dictionary ( we saw this in the dictionary lecture)
# 
# * Check if a key already exists in a dictionary. You can do so with the 'in' keyword. For example, try the following two lines of code in the console. The second line will return True since ‘apple’ is a key in the dictionary:
#     
#     myDictionary = {'apple': 1}
#     
#     'apple' in myDictionary
#     
#     
# * Be able to use an if/else statement to do one thing if the key is already in the dictionary, or another if it is not.
# 
# * This question on the assignment is "simple" because it is using the basics, but it is definitely challenging in that it asks you to combine a bunch of basics.
# 

# In[5]:


# First, let's practice splitting a string by spaces:
listOfWordsFromString = 'This is a string that we will split by the spaces'.split(' ')
print(listOfWordsFromString)


# In[6]:


# Second, we will practice checking if a key is already in a dictionary:
myDictionary = {}
myDictionary['the'] = 1

if 'the' in myDictionary:
    print(True)


# In[9]:


# Now, define the function wordCount() in this cell.
def wordCount(myString):
    wordDict = {}
    wordList = myString.split(' ')
    for word in wordList:
        if word in wordDict:
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1
    return wordDict


# In[10]:


# Now, test the function
results = wordCount('I like cats and I like dogs')
print(results)


# In[ ]:




