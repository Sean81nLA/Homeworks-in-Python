#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1 A for loop that loops 10 times and prints the number of each loop,
#starting at 0. That is, it prints the numbers 0 through 9.

#a. Hint, you can use the range() function just like we did in lecture

for number in range(10):
    print(number)


# In[37]:


#2. A for loop that loops 10 times and prints the number a number on each loop 
#from 0 through 9 (just like problem #1). On each loop it will print ‘zero’,
#‘even’ or ‘odd’. It will print ‘zero’ if the number is 0, ‘even’ if the number
#is even, and ‘odd’ if odd.

#a. Hint: Use the modulo operator to test if a number is even. The modulo 
#will result in 0 since 0 is the remainder of 4 divided by 2. You can test 
#this by putting the following code in a cell in a notebook and running the 
#cell.


for n in range(10):
    if n % 2==0 and n==0:
        print('zero')
    elif n%2==0 and n!=0:
         print('even')
    else:
        print('odd')
   


# In[4]:


#3. Create a variable, ‘myVar’, with the value 2.0. Then write a while loop that multiplies
#increases the value of 'myVar' by a factor of 1.65 on each loop (That is, it multiplies the
#value by 1.65). The while loop will continue until myVar is greater than 100. After the
#while loop is complete, print the value of myVar

myVar = 2.0
while myVar < 100:
    myVar = myVar * 1.65  
print(myVar)

