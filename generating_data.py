#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np
import json


# In[10]:


arr = [num for num in range(0, 100000000) if random.uniform(0,1) >= 0.5]
x = random.randint(0, 100000000)
n = len(arr)

print ('Length of array',n)
print ('Target value',x)


# In[11]:


out_data = {'data': arr, 'target': x}
with open('input.json', 'w') as f:
    json.dump(out_data, f)


# In[ ]:




