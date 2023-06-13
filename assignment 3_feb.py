#!/usr/bin/env python
# coding: utf-8

# In[9]:


##Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.

##The keyword used to create a function in Python is "def".
##list of odd numbers in the range of 1 to 25:
def get_odd_number():
    odd_number=[]
    for i in range (1,26):
        if i%2!=0:
            odd_number.append(i)
    return odd_number


# In[10]:


get_odd_number()


# In[13]:


#why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use.

#*args and **kwargs are special syntax in Python that allow you to pass a variable number of arguments to a function.
#*args is used to pass a variable number of non-keyworded arguments to a function. It allows you to pass any number of arguments to the function, and the function will receive them as a tuple.
#**kwargs is used to pass a variable number of keyworded arguments to a function. It allows you to pass any number of arguments to the function as keyword arguments, and the function will receive them as a dictionary.
def concatenate_strings(*args):
    concatenated_string = 'ram'
    for arg in args:
        concatenated_string += arg
    return concatenated_string


# In[15]:


concatenate_strings(" laxuman")


# In[16]:


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# In[19]:


print_kwargs(name="sangram",college_name="ghrcem",location="satara")


# In[20]:



#An iterator in Python is an object that allows you to iterate over a sequence of values. It provides a way to access the elements of a container (e.g., a list or a dictionary) one at a time, without having to access the entire container at once.

#In Python, to create an iterator object, you can use the iter() method, which takes an iterable object (e.g., a list or a tuple) as an argument and returns an iterator object. Once you have an iterator object, you can use the next() method to iterate through the elements of the iterable.
#Here's an example of using an iterator to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]:


# In[21]:


# Create the iterator object
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_iterator = iter(my_list)

# Iterate through the first five elements
for i in range(5):
    print(next(my_iterator))


# In[22]:


my_list=[2,3,4,5,6,7,8]
my_iterator = iter(my_list)

for i in range(5):
    print(next(my_iterator))


# In[ ]:




