#!/usr/bin/env python
# coding: utf-8

# In[1]:


d={}


# In[2]:


type(d)


# In[3]:


d1={'key':"sangram"}


# In[4]:


d1


# In[5]:


d2={'name':'sangram','email':'sangram@gmail.com','ph_no':32105040}


# In[6]:


d2


# In[12]:


d3={1212:'jeevan','abc':123}


# In[13]:


d3


# In[14]:


d4={@as:'fnn'}


# In[15]:


d5={True:1235}


# In[16]:


d5


# In[17]:


d3['abc']


# In[20]:


d5[1]#here it takking value of key


# In[21]:


d6={'name':"sangram","mail":"sangram@gmail.com",'name':"sam"}


# In[22]:


d6['name']


# In[23]:


d7={"company":'PWSKILLS',"courses":["web_dev","data_science","java_with_dsa"]}


# In[24]:


d7


# In[25]:


d7['courses']


# In[26]:


d7['courses'][2]


# In[27]:


d7['courses'][1]


# In[28]:


d8={'number':[2,3,4,5,6],"assignment":(1,2,3,4,5,6),"launch_date":{23,12,14},"class_time":{"web_dev":8,"datascience":9,"dsa":5}}


# In[41]:


d8


# In[42]:


d8['class_time']


# In[43]:


d8['class_time']['dsa']


# In[44]:


d8['mentor']=["sudhanshu","cris","hyder"]


# In[47]:


d8


# In[49]:


d8['number']=[8,3]


# In[50]:


d8


# In[51]:


del d8['number']


# In[52]:


d8


# In[54]:


d8['assignment']=(1,2,3,4,5,6,7)


# In[61]:


d8


# In[62]:


d8.keys()


# In[63]:


list(d8.keys())


# In[65]:


d8.pop( )


# In[85]:


marks=int(input('enter your marks'))
if marks>= 80:
    print("you will part of A1 batch")
elif marks>= 60 and marks< 80:
    print("you will be part of A2 batch")
elif marks>= 40 and marks< 60:
    print("you will be part of A3 batch")
elif marks>= 0 and marks< 40:
    print("you will be part of A3 batch")
else:
    print("not eligible ")


# In[86]:


10>=80


# In[87]:


type(marks)


# In[89]:


price=int(input("enter price "))
if price>1000:
    print("i will not purchase")
else:
    print("i will purchase")


# In[95]:


price=int(input("enter price "))
if price>1000:
    print("i will not purchase")
    if price>5000:
        print("this is too much")
    elif price<2000:
        print("its okk")


# In[97]:


l=[1,2,3,4,5,6]


# In[98]:


l[0]+1


# In[99]:


l1=[]


# In[100]:


l1.append(l[0]+1)


# In[101]:


l1


# In[102]:


for i in l:
    print(i)


# In[104]:


l1=[]
for i in l:
    print(i+1)
    l1.append(i+1)
l1


# In[105]:


l=["sangram","himanshu","gudu","dada"]


# In[110]:


l1=[]
for i in l:
    print(i)
    l1.append(i.upper())
l1


# In[107]:


l1


# In[111]:


l=[1,2,3,4,5,"sam","bro","abc",123,456]


# In[113]:


l1_num=[]
l2_str=[]
for i in l:
    if type (i)==int or type(i)==float:
        l1_num.append(i)
    else:
        l2_str.append(i)


# In[114]:


l1_num


# In[116]:


l2_str


# In[ ]:




