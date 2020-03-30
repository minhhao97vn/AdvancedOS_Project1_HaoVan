#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import json


# In[45]:


with open('fibonacci_info_alone.json', 'r') as f:
    fibonacci_info_alone = json.load(f)
with open('fibonacci_info_concurrent.json', 'r') as f:
    fibonacci_info_concurrent = json.load(f)
with open('jump_info_alone.json', 'r') as f:
    jump_info_alone = json.load(f)
with open('jump_info_concurrent.json', 'r') as f:
    jump_info_concurrent = json.load(f)


# In[46]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x_axis = ['fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent']
running_time_algo = [float(fibonacci_info_alone['run_time_algo']), float(jump_info_alone['run_time_algo']), float(fibonacci_info_concurrent['run_time_algo']), float(jump_info_concurrent['run_time_algo'])]
ax.bar(x_axis,running_time_algo)
plt.ylabel('seconds')
plt.title('Running time for algorithm only')
# plt.show()


# In[47]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x_axis = ['fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent']
running_time_prog = [float(fibonacci_info_alone['run_time_prog']), float(jump_info_alone['run_time_prog']), float(fibonacci_info_concurrent['run_time_prog']), float(jump_info_concurrent['run_time_prog'])]
ax.bar(x_axis,running_time_prog)
plt.ylabel('seconds')
plt.title('Running time for program')
# plt.show()


# In[48]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x_axis = ['fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent']
running_time_prog = [float(fibonacci_info_alone['CPU_perc']), float(jump_info_alone['CPU_perc']), float(fibonacci_info_concurrent['CPU_perc']), float(jump_info_concurrent['CPU_perc'])]
ax.bar(x_axis,running_time_prog)
plt.ylabel('percentage')
plt.title('CPU percentages for program')
# plt.show()


# In[49]:


data = [[float(fibonacci_info_alone['RSS_algo']), float(jump_info_alone['RSS_algo']), float(fibonacci_info_concurrent['RSS_algo']), float(jump_info_concurrent['RSS_algo'])],
[float(fibonacci_info_alone['VMS_algo']), float(jump_info_alone['VMS_algo']), float(fibonacci_info_concurrent['VMS_algo']), float(jump_info_concurrent['VMS_algo'])],
[fibonacci_info_alone['pagefaults_algo'], jump_info_alone['pagefaults_algo'], fibonacci_info_concurrent['pagefaults_algo'], jump_info_concurrent['pagefaults_algo']],
[fibonacci_info_alone['pageins_algo'], jump_info_alone['pageins_algo'], fibonacci_info_concurrent['pageins_algo'], jump_info_concurrent['pageins_algo']]]
x_axis = ['fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent']
fig = plt.figure()
X = np.arange(4)
ax = fig.add_axes([0,0,1,1])
ax.bar(X , data[0], color = 'b', width = 0.25)
ax.bar(X+0.25 , data[1], color = 'g', width = 0.25)
# ax.bar(x_axis , data[2], color = 'r', width = 0.25)
# ax.bar(x_axis , data[3], color = 'y', width = 0.25)

ax.legend(['RSS', 'VMS'])
ax.set_ylabel('GB')
plt.xticks(X+0.25, ('fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent'))
plt.title('RSS and VMS for running algorithm')
# plt.show()


# In[50]:


data = [[float(fibonacci_info_alone['RSS_prog']), float(jump_info_alone['RSS_prog']), float(fibonacci_info_concurrent['RSS_prog']), float(jump_info_concurrent['RSS_prog'])],
[float(fibonacci_info_alone['VMS_prog']), float(jump_info_alone['VMS_prog']), float(fibonacci_info_concurrent['VMS_prog']), float(jump_info_concurrent['VMS_prog'])]]
x_axis = ['fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent']
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X, data[0], color = 'b', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)

# print(data)

ax.legend(['RSS', 'VMS'])
ax.set_ylabel('GB')
plt.xticks(X+0.25, ('fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent'))
plt.title('RSS and VMS for running program')
# plt.show()


# In[54]:


data = [[fibonacci_info_alone['pagefaults_algo'], jump_info_alone['pagefaults_algo'], fibonacci_info_concurrent['pagefaults_algo'], jump_info_concurrent['pagefaults_algo']],
[fibonacci_info_alone['pageins_algo'], jump_info_alone['pageins_algo'], fibonacci_info_concurrent['pageins_algo'], jump_info_concurrent['pageins_algo']]]

x_axis = ['fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent']
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X, data[0], color = 'b', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)

print(data)

ax.legend(['Pagefaults', 'Pageins'])
ax.set_ylabel('counts')
plt.xticks(X+0.25, ('fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent'))
plt.title('Pagefaults and pageins for running algorithm')
# plt.show()


# In[55]:


data = [[fibonacci_info_alone['pagefaults_prog'], jump_info_alone['pagefaults_prog'], fibonacci_info_concurrent['pagefaults_prog'], jump_info_concurrent['pagefaults_prog']],
[fibonacci_info_alone['pageins_prog'], jump_info_alone['pageins_prog'], fibonacci_info_concurrent['pageins_prog'], jump_info_concurrent['pageins_prog']]]

x_axis = ['fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent']
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X, data[0], color = 'b', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)

print(data)

ax.legend(['Pagefaults', 'Pageins'])
ax.set_ylabel('counts')
plt.xticks(X+0.25, ('fibonacci_alone', 'jump_alone', 'fibonacci_concurrent', 'jump_concurrent'))
plt.title('Pagefaults and pageins for running program')
plt.show()


# In[ ]:




