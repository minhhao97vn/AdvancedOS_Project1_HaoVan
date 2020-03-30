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


# # Import data

# In[2]:


with open('input.json', 'r') as f:
    input_data = json.load(f)

arr = input_data['data']
target = input_data['target']


# # Algorithm

# In[3]:


def jump_search(arr, x, n): 
      
    step = math.sqrt(n) 
      
    prev = 0
    while arr[int(min(step, n)-1)] < x: 
        prev = step 
        step += math.sqrt(n) 
        if prev >= n: 
            return -1
      
    while arr[int(prev)] < x: 
        prev += 1
          
        if prev == min(step, n): 
            return -1
      
    if arr[int(prev)] == x: 
        return prev 
      
    return -1


# In[4]:


def run_jump_search(arr, x, n, info_out_file):
    print ("Running Jump Search ...")
        
    start_time_algorithm = time()
    start_mem = ps.memory_info()

    index = jump_search(arr, x, n) 
    
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
    print("RSS for running algorithm only:", '{0:.10f}'.format((end_mem.rss-start_mem.rss)/2.**30))
    print("RSS for running program:", '{0:.10f}'.format((end_mem.rss)/2.**30))
    print()
    print("VMS for running algorithm only:", '{0:.10f}'.format((end_mem.vms-start_mem.vms)/2.**30))
    print("VMS for running program:", '{0:.10f}'.format((end_mem.vms)/2.**30))
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


run_jump_search(arr, target, len(arr), 'jump_info_alone')

