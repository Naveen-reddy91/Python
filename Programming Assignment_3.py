#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[11]:


num = float(input("Enter the number: ")) #Input

if num == 0:
    print("The entered value is Zero")
elif number > 0:
    print ("The entered value is Positve number")
else:
    print ("The entered value is Negative number ")


# 2. Write a Python Program to Check if a Number is Odd or Even?

# In[26]:


num = int(input("Enter the number: ")) #Input

if num % 2 == 0:
    print(num, " is a  Even Number")
else:
    print(num,  "is an Odd Number")


# 3. Write a Python Program to Check Leap Year?

# In[27]:


year = int(input("Enter the year: "))

if year % 4 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


# 4. Write a Python Program to Check Prime Number?

# In[29]:


num = int(input("Enter the number: "))

if num > 1:
    
    for i in range(2, num):
        
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[31]:


lower = int(input("Enter the lower interval: "))
upper = int(input("Enter the upper interval: "))

for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num):
            if (num%i) == 0:
                break
        else:
            print(num)


# In[ ]:




