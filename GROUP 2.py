#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr = np.array ([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(3,4)


# In[3]:


a = 5
b =6
c = a + b
c


# In[6]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr


# In[9]:


newarray = arr.reshape(4,3)


# In[10]:


newarray


# In[11]:


fArray = np.array([[ 1,  2,  3],[ 4,  5,  6],[ 7,  8,  9], [10, 11, 12]])
newfArray = fArray.reshape(-1)


# In[12]:


newfArray


# In[14]:


arr = np.array([[ 1,  2,  3, 4,  5,  6],[ 7,  8,  9, 10, 11, 12]])
print(arr)


# # access element in the first row and second column 

# In[15]:


arr[1,5]


# In[16]:


arr[0,1] + arr[0,5]


# In[23]:


for x in arr:
    for y in x:
        print(y)
       


# In[24]:


arr = np.array([[ 1,  2,  3, 4,  5,  6],[ 7,  8,  9, 10, 11, 12]])
print(arr[1, 1:5])


# In[25]:


arr[2:]


# In[29]:


print(arr[1, 2:])


# In[34]:


arr = np.array([ 1,  2,  3, 4,  5,  6, 7,  8,  9, 10, 11, 12])
x = np.where(arr%2==0)
print(x)


# In[35]:


get_ipython().system('pip install pandas')


# In[4]:


import pandas as pd
li = [3, 4, 7, 44,32,667,322,43, 32, 32]
ans = pd.Series(li)
print(ans)


# In[12]:


import pandas as pd
dic = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}
result = pd.Series(dic)
result


# In[4]:


import pandas as pd
data = {
    "S/N": [1,2,3,4,5],
    "color" : ["red", "yellow", "Green", "Blue", "Orange"]
}
result = pd.DataFrame(data)
print(result)

import pandas as pd
data = {
    "S/N": [1,2,3,4,5],
    "color" : ["red", "yellow", "Green", "Blue", "Orange"],
    "names": ["James", "Oluwakemisola", "Bukoa", "Mike", "Isaac"]
}
resut = pd.DataFrame(data)
result

# In[2]:


import pandas as pd
data = {
    "S/N": [1,2,3,4,5],
    "color" : ["red", "yellow", "Green", "Blue", "Orange"],
    "names": ["James", "Oluwakemisola", "Bukoa", "Mike", "Isaac"]
}
result = pd.DataFrame(data)
result


# In[4]:


result.loc[2]


# In[6]:


import pandas as pd
data = {
    "S/N": [1,2,3,4,5],
    "color" : ["red", "yellow", "Green", "Blue", "Orange"],
    "names": ["James", "Oluwakemisola", "Bukoa", "Mike", "Isaac"]
}
result = pd.DataFrame(data)
result


# In[12]:


import pandas as pd
df = pd.read_csv("C:/Users/USER/Desktop/python prac/business.csv")
print(df.info())


# In[15]:


import pandas as pd
df = pd.read_csv("C:/Users/USER/Desktop/python prac/business.csv")
print(df.describe())


# In[17]:


df.head(10)


# In[19]:


df.tail(30)


# In[25]:


print(df.head(5), df.tail(5))


# In[29]:


import pandas as pd
dd = pd.read_csv("C:/Users/USER/Desktop/python prac/business.csv")
print(dd.describe())


# In[33]:


print(dd.head(4))


# In[34]:


dd.info()


# In[35]:


get_ipython().system('pip install matplotlib')


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,8])
y = np.array([0, 80])
plt.plot(x,y)
plt.show()


# Line Chart
# 

# In[8]:


import matplotlib.pyplot as plt
import numpy as np
points = np.array([2, 3,2,3,2,7])
plt.plot(points)
plt.show()


# In[11]:


points2 = np.array([1,2,32,3,2,45,2,1,3,2,4,4])
plt.plot(points2, linestyle ="solid")
plt.show()


# BAR CHAT

# In[14]:


x = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
y = np.array([23, 26, 30, 35, 45, 50])
plt.bar(x,y)
plt.show()


# SCATTER PLOT

# In[16]:


import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([2,3,4,7,6,5])
y1 = ([4, 11, 3, 12, 8,9])
plt.scatter(x1, y1)
plt.show()


# PIE CHART

# In[20]:


y = np.array([32,54,11,34,24,24])
plt.pie(y)


# HISTOGRAM

# In[27]:


x = np.random.normal(170, 10, 250)
plt.hist(x)


# In[28]:


get_ipython().system('pip install seaborn')


# In[30]:


import seaborn as sns
import matplotlib.pyplot as plt


# ## BOXPLOT

# In[32]:


import pandas as dp
df = sns.load_dataset("tips")
df


# In[35]:


df.boxplot(by = 'day', column = ['total_bill'], grid= False)


# In[37]:


titanic = sns.load_dataset("titanic")
titanic


# In[9]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as np
titanic = sns.load_dataset("titanic")
titanic.head(15)


# In[7]:


age1 = titanic['age'].dropna()
sns.displot(age1,bins=30,kde = False )


# In[15]:


data = sns.load_dataset('mpg')
data.head()


# In[18]:


sns.regplot(x='mpg', y= 'acceleration', data = data)
plt.show()


# In[20]:


w = data.head()
w


# In[21]:


sns.regplot(x='mpg', y= 'acceleration', data = w)
plt.show()


# In[9]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as np
df = sns.load_dataset("titanic")
df.tail(15)


# In[5]:


df.isnull().sum()


# In[12]:


df["age"] = df["age"].fillna(df["age"].mode()[0])
df.isnull().sum()


# In[15]:


df['embarked'] = df['embarked'].fillna('S')
df['deck'] = df['deck'].fillna("C")
df['embark_town'] = df['embark_town'].fillna('Chelsea')
df.isnull().sum()


# ## ONE HOT ENCODING

# In[22]:


import pandas as pd
df= pd.read_csv('C:/Users/USER/Desktop/python prac/business.csv')
df.head()


# In[24]:


df['Data_value'].value_counts()


# In[25]:


pd.get_dummies(df,columns = ['Data_value'])


# In[2]:


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


# In[3]:


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




