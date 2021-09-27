#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_excel('Livongo Mini Challege Q3.xlsx')


# In[3]:


df.info()


# In[4]:


df.head()


# In[5]:


df.describe()


# In[13]:


df.corr()


# In[15]:


sns.heatmap(df.corr(), cmap='coolwarm', annot=True)


# In[12]:


sns.pairplot(df,hue='gender',palette='coolwarm')


# In[7]:


avg_bg_checks = df.groupby('gender')['bg_checks'].mean()
avg_bg_checks


# In[9]:


avg_bg_value = df.groupby('gender')['avg_bg_value'].mean()
avg_bg_value


# In[10]:


avg_count_hyper = df.groupby('gender')['count_hyper_reading'].mean()
avg_count_hyper


# In[11]:


avg_count_hypo = df.groupby('gender')['count_hypo_reading'].mean()
avg_count_hypo


# In[27]:


sns.jointplot(x='avg_bg_value',y='count_hyper_reading', data=df, kind='reg')


# In[28]:


sns.jointplot(x='avg_bg_value',y='count_hypo_reading', data=df, kind='reg')


# In[ ]:




