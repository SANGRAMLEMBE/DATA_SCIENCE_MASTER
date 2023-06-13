#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[1,2,3,4,5,6]


# In[3]:


for i in l:
    print(i,type(i))


# In[4]:


l1=["sangram","jeevan","himanshu","gudu"]


# In[13]:


for i in l1:
    print(i)


# In[14]:


l1


# In[15]:


for i in l1:
    print(i)
else:
    print("if for loop will exicuted then only else loop exicuted")


# In[16]:


for i in l1:
    if i=="himanshu":
        break
    print(i)


# In[20]:


l1
for i in l1:
    if i=='jeevan':
        break
    print(i)
else:
    print("exicute this if for loop is able to complete itself")
    


# In[18]:


l1


# In[21]:


for i in l1:
    if i=='jeevan':
        continue
    print(i)


# In[22]:


for i in l1:
    if i=='jeevan':
        continue
    print(i)
else:
    print("execute this if for loop is able to complete itself")


# In[23]:


range(5)


# In[24]:


list(range(0,5))


# In[25]:


list(range(0,5,1))


# In[26]:


list(range(0,20,2))


# In[28]:


list(range(-10,0))


# In[30]:


len(l1)


# In[32]:


list(range(len(l1)))


# In[33]:


for i in range(len(l1)):
    print (l1[i])


# In[37]:


for i in range(len(l1)-1,-1,-1):
    print(l1[i])#### lower bond  , upper bond   ,  jump


# In[38]:


l2=[23,45,56,75,85,96,52,63,41,507,7,89,520]


# In[39]:


range(0,len(l2))


# In[41]:


list(range(0,len(l2),2))


# In[43]:


for i in range(0,len(l2),2):
    print(l2[i])


# In[44]:


l2[0]


# In[45]:


l


# In[46]:


result=0
for i in l:
    result=result+i
result


# In[47]:


sum(l)


# In[48]:


t=(1,2,3,4,5,6,7)


# In[49]:


for i in t:
    print(i)


# In[51]:


result=0
for i in t:
    result=result+i
result


# In[61]:


s={"sangram",1,2,3,4,"pwskills"}


# In[63]:


for i in s:
    print(i)


# In[64]:


s


# In[65]:


for i in s:
    print(i)

    


# In[67]:


sam={11,20,45,6585,"sangram",120,58,75,"jeevan"}


# In[68]:


for i in sam:
    print(i)


# In[69]:


s1="pwskills"


# In[70]:


for i in s1:
    print(i)


# In[72]:


d={"name":"sangram","class":"dsm","topic":["python","sets","machine learnning","nlp"]}


# In[73]:


d['name']


# In[74]:


d.keys()


# In[75]:


for i in d.keys():
    print(d[i])


# In[76]:


d.values()


# In[79]:


for i in d.values():
    print(i)


# In[81]:


d.items()


# In[82]:


for i in d.items():
    print(i)


# In[ ]:




