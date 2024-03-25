#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import time

def server_load_simulation(mean_load, mean_processing_time, simulation_duration):
    """
    Simulate server load using Poisson distribution with processing time for each request.
    
    Parameters:
        mean_load (float): Mean load on the server.
        mean_processing_time (float): Mean processing time for each request.
        simulation_duration (int): Duration of simulation in seconds.
    """
    start_time = time.time()
    end_time = start_time + simulation_duration

    while time.time() < end_time:
        # Generate a random number based on Poisson distribution for load
        load = np.random.poisson(mean_load)
        
        # Generate a random number based on exponential distribution for processing time
        processing_time = np.random.exponential(mean_processing_time)
        
        print(f"Server Load: {load}, Processing Time: {processing_time:.2f} seconds")
        
        time.sleep(1)  # Simulate 1 second interval

if __name__ == "__main__":
    mean_load = float(input("Enter the mean load on the server: "))
    mean_processing_time = float(input("Enter the mean processing time for each request (in seconds): "))
    simulation_duration = int(input("Enter the duration of simulation in seconds: "))
    server_load_simulation(mean_load, mean_processing_time, simulation_duration)


# In[3]:


import matplotlib.pyplot as plt

# Data provided
server_data = [
    {"load": 97, "processing_time": 2.66},
    {"load": 143, "processing_time": 7.97},
    {"load": 140, "processing_time": 0.29},
    {"load": 103, "processing_time": 2.70},
    {"load": 116, "processing_time": 0.93},
    {"load": 108, "processing_time": 0.78},
    {"load": 111, "processing_time": 3.72},
    {"load": 120, "processing_time": 5.55},
    {"load": 114, "processing_time": 1.53},
    {"load": 128, "processing_time": 0.22}
]

# Extracting loads and processing times
loads = [data["load"] for data in server_data]
processing_times = [data["processing_time"] for data in server_data]

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(loads, processing_times, marker='o', linestyle='-')
plt.xlabel('Load')
plt.ylabel('Processing Time (seconds)')
plt.title('Load vs Processing Time')
plt.grid(True)
plt.show()


# In[ ]:




