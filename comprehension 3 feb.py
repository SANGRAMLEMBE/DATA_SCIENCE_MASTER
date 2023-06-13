#!/usr/bin/env python
# coding: utf-8

# In[2]:


l=[1,2,3,4,5]
l1=[]
for i in l:
    l1.append(i**2)


# In[3]:


l1


# In[4]:


l


# In[5]:


[i**2 for i in l]


# In[6]:


l


# In[9]:


[i for i in l if i%2==0]


# In[10]:


l1=["sangram","jeevan","tejas","nidhi"]


# In[11]:


[i.upper() for i in l1]


# In[12]:


l


# In[13]:


(i**2 for i in l)#here gendrater operater is gendrated.


# In[14]:


list(i**2 for i in l)


# In[15]:


d={"key1":1,"key2":2,"key3":3,"key4":4}


# In[18]:


{k:v**2 for k,v in d.items()}


# In[17]:


d.items()


# In[19]:


{k:v for k,v in d.items() if v>1}


# In[ ]:




