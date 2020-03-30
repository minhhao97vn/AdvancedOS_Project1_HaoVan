#!/usr/bin/env python
# coding: utf-8

# In[1]:


from time import time
import psutil
import os

# Initialization
start_time_program = time()
pid = os.getpid()
ps = psutil.Process(pid)
start_cpu_percent_program = ps.cpu_percent()

import json
import math
from bisect import bisect_left


# # Import data

# In[2]:


with open('input.json', 'r') as f:
    input_data = json.load(f)

arr = input_data['data']
target = input_data['target']


# # Algorithm

# In[3]:


def fibonacci_search(arr, x, n): 

    fibMMm2 = 0 
    fibMMm1 = 1 
    fibM = fibMMm2 + fibMMm1
  
    while (fibM < n): 
        fibMMm2 = fibMMm1 
        fibMMm1 = fibM 
        fibM = fibMMm2 + fibMMm1 
  
    offset = -1; 
  
    while (fibM > 1): 
          
        i = min(offset+fibMMm2, n-1) 
  
        if (arr[i] < x): 
            fibM = fibMMm1 
            fibMMm1 = fibMMm2 
            fibMMm2 = fibM - fibMMm1 
            offset = i 
  
        elif (arr[i] > x): 
            fibM = fibMMm2 
            fibMMm1 = fibMMm1 - fibMMm2 
            fibMMm2 = fibM - fibMMm1 
  
        else : 
            return i 
  
    if(fibMMm1 and arr[offset+1] == x): 
        return offset+1; 
  
    return -1


# In[4]:


def run_fibonacci_search(arr, x, n, info_out_file):
    print ("Running Fibonacci Search ...")
    
    
    start_cpu_percent_algorithm = ps.cpu_percent()
    start_time_algorithm = time()
    start_mem = ps.memory_info()

    index = fibonacci_search(arr, x, n) 
    
    end_cpu_percent = ps.cpu_percent()
    end_time = time()
    end_mem = ps.memory_info()
    
    print("Result: number" , x, "is at index" ,"%.0f"%index) 
    print()
    print("Running time of algorithm:",'{0:.10f}'.format(end_time-start_time_algorithm))
    print("Running time of program:",'{0:.10f}'.format(end_time-start_time_program))
    print()
    print("CPU percent for running program:", end_cpu_percent-start_cpu_percent_program)
    print()
    print("RSS for running algorithm only (GB):", '{0:.10f}'.format((end_mem.rss-start_mem.rss)/2.**30))
    print("RSS for running program (GB):", '{0:.10f}'.format((end_mem.rss)/2.**30))
    print()
    print("VMS for running algorithm only (GB):", '{0:.10f}'.format((end_mem.vms-start_mem.vms)/2.**30))
    print("VMS for running program (GB):", '{0:.10f}'.format((end_mem.vms)/2.**30))
    print()
    print("Page faults for running algorithm only:", end_mem.pfaults-start_mem.pfaults)
    print("Page faults for running program:", end_mem.pfaults)
    print()
    print("Page ins for running algorithm only:", end_mem.pageins-start_mem.pageins)
    print("Page ins for running program:", end_mem.pageins)
    
    out_results = {
        'run_time_algo': '{0:.10f}'.format(end_time-start_time_algorithm),
        'run_time_prog': '{0:.10f}'.format(end_time-start_time_program),
        'CPU_perc': end_cpu_percent-start_cpu_percent_program,
        'RSS_algo': '{0:.10f}'.format((end_mem.rss-start_mem.rss)/2.**30),
        'RSS_prog': '{0:.10f}'.format((end_mem.rss)/2.**30),
        'VMS_algo': '{0:.10f}'.format((end_mem.vms-start_mem.vms)/2.**30),
        'VMS_prog': '{0:.10f}'.format((end_mem.vms)/2.**30),
        'pagefaults_algo': end_mem.pfaults-start_mem.pfaults,
        'pagefaults_prog': end_mem.pfaults,
        'pageins_algo': end_mem.pageins-start_mem.pageins,
        'pageins_prog': end_mem.pageins
    }
    
    with open(info_out_file+'.json', 'w') as f:
        json.dump(out_results, f)


# In[5]:


run_fibonacci_search(arr, target, len(arr), 'fibonacci_info_alone')


# In[ ]:




