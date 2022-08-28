#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to convert kilometers to miles?

# In[4]:


kilometers = float(input("Enter value in kilometers: ")) #Input

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# 2. Write a Python program to convert Celsius to Fahrenheit?

# In[13]:


Celsius = float(input("Enter value in Celsius: ")) #Input

Fahrenheit = (Celsius * 9/5) + 32

print('%0.2f Celsius is equal to %0.2f Fahrenheit' %(Celsius,Fahrenheit))


# 3. Write a Python program to display calendar?

# In[16]:


import calendar as cl #importing calendar module

#Input

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

#display the calendar

print(cl.month(year, month))


# 4. Write a Python program to solve quadratic equation?

# In[18]:


import cmath

a = 1
b = 5
c = 6

d = (b**2 - 4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)

sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# 5. Write a Python program to swap two variables without temp variable?

# In[17]:


x = 4
y = 8

x,y = y, x

print("x ", x)
print("y ", y)


# In[ ]:




