#!/usr/bin/env python
# coding: utf-8

# In[80]:


print("this is my print")


# In[81]:


l=[12,10,30,45,78]


# In[82]:


len(l)


# In[83]:


type(l)


# In[84]:


def test1():
    print("hey ,here is 1st function")


# In[85]:


test()


# In[86]:


def test2():
    return"this is your 1st function"


# In[87]:


test2()+" sangram"


# In[88]:


def test3():
    return"sangram",21,56.25,[1,2,3,3]


# In[89]:


test3()


# In[90]:


a,b,c,d=test3()


# In[91]:


a


# In[92]:


b


# In[93]:


c


# In[94]:


d


# In[95]:


a=1
b=4


# In[96]:


a,b=1,4


# In[97]:


def test4():
    a=5+6/7
    return a


# In[98]:


test4()


# In[99]:


def test5(a,b,c):
    d=a+b+c
    return d


# In[100]:


test5()


# In[101]:


test5(2,5,6)


# In[102]:


def test6(a,b):
    return a+b


# In[103]:


test6(5,10)


# In[104]:


test6("sangram"," jeevan")


# In[105]:


test6([1,2,3,4],[4,5,6,7])


# In[106]:


l=[1,2,3,4,"sam","gudu",[7,4,5]]


# In[107]:


l1=[]
for i in l:
    if type(i)==int or type(i)==float:
        l1.append(i)


# In[108]:


l1


# In[109]:


def test7(l):
    l1 = []
    for i in l:
        if type(i)==int or type(i)==float:
            l1.append(i)
            
    return l1
    


# In[110]:


test7(l)


# In[132]:


li=[7,5,2,6,"sam",[1,2]]


# In[134]:


test7(li)


# In[140]:


def test8(a):
    l1=[]
    for i in a :
        if type(i) == list:
            for j in i:
                l1.append(j)
        else:
            if type(i) == int or type(i) == float:
                l1.append(i)
    return l1


# In[141]:


l


# In[142]:


test8(l)


# In[143]:


k=[[3,4,6],"sam"]


# In[144]:


test8(k)# here we have the  output as 3,4,6 , but in this case this is showing wrong"


# In[145]:


def test9(a):
    """ this is my function to extract num data from list"""
    l1=[]
    for i in a :
        if type(i) == list:
            for j in i:
                l1.append(j)
        else:
            if type(i) == int or type(i) == float:
                l1.append(i)
    return l1


# In[147]:


test9(l)#to check docstring press shift and tab


# In[149]:


def test10(a,b):
    return a+b


# In[151]:


def test11(*args):
    return args


# In[153]:


test11(1,2,3)


# In[154]:


test11(1,2,3,"sam","gudu",[1,2,3,4])


# In[155]:


def test12(*sam):
    return sam


# In[156]:


test12(1,2,54,96)


# In[157]:


def test13(*args,a):
    return args,a


# In[158]:


test13(1,2,3,4)#here it gate confuesed


# In[159]:


test13(1,2,3,4,a=23)#when we  declair properly then it shows proper output.


# In[160]:


def test14(c,d,a=12,b=10):
    return a,b,c,d


# In[161]:


test14(5,6)#here we have a and b value from given we want only value of c, d


# In[162]:


test14(2,5,a=456)


# In[163]:


def test15(**kwargs):
    return kwargs


# In[164]:


test15()


# In[165]:


type(test15())


# In[166]:


test15(a=12,b=[1,2,3],c=23.45)


# In[ ]:




