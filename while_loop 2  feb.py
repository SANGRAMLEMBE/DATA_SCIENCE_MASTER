#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=1  
while a<=10:
    print(a)
    a=a+1


# In[7]:


#sum up the no  till sum point

n=int(input("enter your limit "))
strting_point=0
counter=1

while counter<=n:
    strting_point=strting_point+counter
    counter=counter+1
strting_point


# In[4]:


n=int(input("enter your limit "))
strting_point=0
counter=1

while counter<=n:
    strting_point=strting_point+counter
    counter=counter+1
strting_point


# In[11]:


### factorial 


number=int(input("enter your number"))
factorial=1
while number>0:
    factorial =factorial *number
    number=number-1
factorial


# In[ ]:


##fibonancii series


# In[14]:


number=int(input("enter the nuber of element you are looking for"))
a,b=0,1
counter=0
while counter<number:
    print(a)
    c=a+b
    a=b
    b=c
    counter=counter+1


# In[15]:


a,b=0,1
for i in range(10):
    print(a)
    c=a+b
    a=b
    b=c
    


# In[16]:


s="sangram"
s[::-1]


# In[25]:


word=input("enter your string for reverse ")


# In[23]:


reverse=""
length=len(word)
while length>0:
    reverse==reverse + word[length -1]
    length=length-1
print(reverse)
    


# In[27]:


reverse=""
length=len(word)
while length>0:
    reverse=reverse + word[length -1]
    length=length-1
print(reverse)


# In[30]:


n=int(input("enter your number"))
i=1
while i<=10:
    result=n*i
    print(n,"* ",i,"= ",result)
    i=i+1


# In[32]:


n=5
i=1
while i<n:
    print(i)
    i=i+1
else:
    print("this will be excuted once your while will complete it succesfully")


# In[ ]:




