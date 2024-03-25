#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import time

class Server:
    def __init__(self, id):
        self.id = id
        self.load = 0
        self.processing_time = 0

    def process_load(self, load):
        self.load += load
        self.processing_time = self.load * 0.1  # Processing time is proportional to the load

    def __str__(self):
        return f"Server {self.id}: Load={self.load}, Processing Time={self.processing_time:.2f} seconds"

class Compiler:
    def __init__(self, num_servers):
        self.servers = [Server(i) for i in range(num_servers)]
        self.loads_assigned = 0

    def assign_load(self, load):
        min_server = min(self.servers, key=lambda server: server.processing_time)
        min_server.process_load(load)
        print(f"Assigned load {load} to {min_server}")
        self.loads_assigned += 1

if __name__ == "__main__":
    num_servers = 3  # Number of servers
    compiler = Compiler(num_servers)
    max_loads = 10  # Maximum loads to assign

    while compiler.loads_assigned < max_loads:
        load = random.randint(1, 10)  # Random load between 1 and 10
        compiler.assign_load(load)
        time.sleep(1)  # Simulate some time passing between load assignments

    print("Maximum loads assigned. Terminating program.")


# In[ ]:





# ### 

# In[7]:


import matplotlib.pyplot as plt

# Data provided
assignments = [
    (7, 0.70),
    (8, 0.80),
    (10, 1.00),
    (9, 0.90),
    (16, 1.60),
    (17, 1.70),
    (19, 1.90),
    (22, 2.20),
    (21, 2.10),
    (24, 2.40)
]

# Summarize data into load and time
load = []
time = []
total_time = 0

for l, t in assignments:
    load.append(l)
    total_time += t
    time.append(total_time)

# Plotting
plt.plot(time, load, marker='o')
plt.title('Load vs Time Process')
plt.xlabel('Time (seconds)')
plt.ylabel('Load')
plt.grid(True)
plt.show()


# In[ ]:




