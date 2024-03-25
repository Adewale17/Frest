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

    loads = [44, 61, 54, 89, 64, 93, 104]
    
    for server, load in zip(server_objects, loads):
        server.assign_load(load)


# In[2]:


import matplotlib.pyplot as plt

# Provided output
output = [
    ("Server 1", 44, 0.44941),
    ("Server 2", 61, 0.62352),
    ("Server 3", 54, 0.55391),
    ("Server 4", 89, 0.89860),
    ("Server 5", 64, 0.64242)
]

# Extract load and time data
loads = [entry[1] for entry in output]
processing_times = [entry[2] for entry in output]

# Plot load against time
plt.figure(figsize=(10, 6))
plt.plot(processing_times, loads, marker='o', linestyle='-', color='b')
plt.title('Load vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Load')
plt.grid(True)
plt.show()


# In[ ]:




