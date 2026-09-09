#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
data = {'Name':['Tom', 'nick', 'krish', 'jack'],'Age':[20, 21, 19, 18]}
df = pd.DataFrame(data) 
print(df)


# In[2]:


data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
'Age':[27, 24, 22, 32],
'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data)
print(df[['Name', 'Qualification']])


# In[7]:


data = pd.read_csv("/home/mca/Desktop/sneha/files/archive/Employee.csv")
data.info()


# In[8]:


data.head()


# In[9]:


first = data.head()
print(first)


# In[10]:


import pandas as pd
import numpy as np
arr=np.array([10,15,18,22])
s = pd.Series(arr)
print(s)


# In[11]:


arr=np.array(['a','b','c','d'])
s=pd.Series(arr, index=['first','second','third','fourth'])
print(s)


# In[12]:


s=pd.Series(50, index=[0, 1, 2, 3, 4])
print (s)


# In[13]:


d={'Name': 'Deepthi', 'Class' : 'MCA', 'year' : 2014}
s=pd.Series(d)
print(s)


# In[14]:


s = pd.Series([10,15,18,22])
df=pd.DataFrame(s)
df.columns=['List1']
df['List2']=20
df['List3']=df['List1']+df['List2']
print(df)


# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
values = np.random.randn(100)
s = pd.Series(values) 
print("series\n",s)
s.plot(kind='hist', title='Normally distributed random values')
plt.show()


# In[16]:


s.describe()


# In[17]:


df = pd.DataFrame({'A': [1, 2, 1, 4, 3],
'B': [12, 14, 11, 16, 18],
'C': ['a', 'a', 'b', 'a', 'b']})
df


# In[18]:


df.describe()


# In[19]:


import pandas
iris = pandas.read_csv('/home/mca/Desktop/sneha/files/archive/Employee.csv')
print(iris)


# In[20]:


import pandas as pd
iris = pd.read_csv('/home/mca/Desktop/sneha/files/archive/Employee.csv')
print(iris.head())


# In[21]:


import pandas as pd
df = pd.DataFrame(pd.read_csv("/home/mca/Desktop/sneha/files/archive/Employee.csv"))
df.hist()


# In[28]:


iris['PaymentTier'].hist()


# In[25]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv ('/home/mca/Desktop/sneha/files/archive/Employee.csv')
data.info()
data.describe()
data.head()


# In[32]:


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('tips')

sns.scatterplot(x='total_bill', y='tip', data=data)

plt.title('Scatter Plot of Total Bill vs. Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()


# In[36]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/home/mca/Desktop/sneha/files/archive/Employee.csv')

plt.figure(figsize=(10, 8))

sns.scatterplot(
    x='Age',
    y='JoiningYear',
    data=data
)

plt.title('Scatter Plot of Age vs. Joining Year')
plt.xlabel('Age')
plt.ylabel('Joining Year')

plt.show()


# In[38]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/home/mca/Desktop/sneha/files/archive/Employee.csv')

plt.figure(figsize=(15, 10))

sns.boxplot(
    x='PaymentTier',
    y='Age',
    data=data
)

plt.title('Box Plot of Age by Payment Tier')
plt.xlabel('Payment Tier')
plt.ylabel('Age')

plt.show()


# In[ ]:




