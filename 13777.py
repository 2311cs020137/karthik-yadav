#!/usr/bin/env python
# coding: utf-8

# # EDA
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf


# In[2]:


data1 = pd.read_csv("NewspaperData.csv")
data1.head()


# In[3]:


data1.info()


# In[4]:


data1.isnull().sum()


# In[5]:


data1.isnull()


# In[6]:


data1.describe()


# In[7]:


plt.figure(figsize=(6,3))
plt.title("Box plot for Daily Sales")
plt.boxplot(data1["daily"], vert = False)


# # observations
# there are no missing values
# the daily column values appears to be right_skewed
# the sunday column values also appear to be right_skewed
# there two outliers in both daily column and also in sunday column as observed from the 

# In[8]:


x=data1["daily"]
y = data1["sunday"]
plt.scatter(data1["daily"], data1["sunday"])
plt.xlim(0, max(x) + 100)
plt.ylim(0, max(y) + 100)
plt.show()


# In[9]:


data1["daily"].corr(data1["sunday"])


# In[10]:


data1[["daily","sunday"]].corr()


# In[14]:


import statsmodels.formula.api as smf
model1 = smf.ols("sunday~daily",data = data1).fit()


# In[15]:


model1.summary()


# In[ ]:




