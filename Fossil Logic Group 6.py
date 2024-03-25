#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

class Server:
    def __init__(self, id):
        self.id = id
        self.loads = []

    def assign_load(self, load):
        start_time = time.time()
        # Simulate processing the load
        time.sleep(load * 0.01)  # Processing time scaled by the load value for demonstration
        end_time = time.time()
        processing_time = end_time - start_time
        self.loads.append((load, processing_time))
        print(f"Server {self.id} is handling load: {load}, processing time: {processing_time:.5f} seconds")

if __name__ == "__main__":
    num_servers = 5  # Number of servers is set to 5

    server_objects = [Server(i) for i in range(1, num_servers + 1)]

    loads = [365, 300, 45, 100, 34, 93, 104]
    
    for server, load in zip(server_objects, loads):
        server.assign_load(load)


# In[ ]:





# In[4]:


import matplotlib.pyplot as plt

# Data from the program output
server_ids = [1, 2, 3, 4, 5]
loads = [365, 300, 45, 100, 34]
processing_times = [3.66217, 3.00301, 0.46442, 1.01502, 0.35591]

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(loads, processing_times, marker='o', linestyle='-')
plt.xlabel('Load')
plt.ylabel('Processing Time (seconds)')
plt.title('Load vs Processing Time')
plt.grid(True)
plt.show()


# In[ ]:




