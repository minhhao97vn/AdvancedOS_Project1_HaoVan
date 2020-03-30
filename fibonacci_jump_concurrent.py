#!/usr/bin/env python
# coding: utf-8

# In[1]:


from multiprocessing import Process
from fibonacci_search import run_fibonacci_search
from jump_search import run_jump_search
import json


# # Import data

# In[2]:


with open('input.json', 'r') as f:
    input_data = json.load(f)

arr = input_data['data']
target = input_data['target']


# In[3]:


Process(target=run_fibonacci_search(arr, target, len(arr), 'fibonacci_info_concurrent')).start()
Process(target=run_jump_search(arr, target, len(arr), 'jump_info_concurrent')).start()


# In[ ]:




