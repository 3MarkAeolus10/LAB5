#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
def grade12():
 
    def cal(op,x,y):
        if op == 0 :
            return (x+y)
        else :
            return (x-y)

    num1=random.randint(0,100)
    num2=random.randint(0,100)
    op_num=random.randint(0,1)
    if op_num==0:
        print(num1,"+",num2)
    else :
        print(num1,"-",num2)
    return cal(op_num,num1,num2)
grade12()


# In[ ]:





# In[ ]:





# In[ ]:




