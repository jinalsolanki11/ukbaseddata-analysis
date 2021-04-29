#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import pandas as pd
import numpy as np


# In[4]:


os.getcwd()


# In[5]:


os.listdir(os.getcwd())


# In[6]:


stop_and_search_df = pd.DataFrame()


# In[7]:


for f in os.listdir(os.getcwd()):
    if "ipynb" not in f:
        print(f)
        for file in os.listdir(f):
            
            if "stop-and-search" in file:
                df = pd.read_csv(os.path.join(os.getcwd(), f, file))
                stop_and_search_df = stop_and_search_df.append(df, ignore_index=True)
        


# In[8]:


stop_and_search_df.head()


# In[9]:


stop_and_search_df.count()


# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[11]:


stop_and_search_df.drop(['Policing operation', 'Latitude', 'Longitude'], axis=1, inplace=True)


# In[12]:


stop_and_search_df.head()


# In[17]:


stop_and_search_df[['year', 'month', 'time']] = stop_and_search_df['Date'].str.split('-', 2, expand=True)


# In[18]:


stop_and_search_df.head()


# In[19]:


stop_and_search_df['Self-defined ethnicity'].value_counts()


# In[20]:


# unique_vals = stop_and_search_df['Self-defined ethnicity'].unique()
# stop_and_search_df['Self-defined ethnicity'].replace(to_replace=unique_vals,
#            value= list(range(len(unique_vals))),
#            inplace=True)


# In[21]:


stop_and_search_df['Gender'].value_counts()


# In[22]:


# unique_vals = stop_and_search_df['Gender'].unique()
# stop_and_search_df['Gender'].replace(to_replace=unique_vals,
#            value= list(range(len(unique_vals))),
#            inplace=True)


# In[23]:


stop_and_search_df.head()


# In[24]:


#sns.jointplot("Self-defined ethnicity", "Gender", data=stop_and_search_df, kind='reg');


# In[25]:


stop_and_search_df.groupby(["Type", "Gender"])['Self-defined ethnicity'].agg('count')


# In[26]:


df = stop_and_search_df.groupby(["Type", "Gender"])['Self-defined ethnicity'].agg('count').to_frame(name = 'count').reset_index()


# In[27]:


df.head()


# In[66]:


sns.catplot(x="Type", y="count", hue="Gender", data=df, kind="box")


# In[67]:


sns.displot(df['count'])


# In[68]:


sns.histplot(df['count'])


# In[31]:


plt.hist(df['count'], alpha=0.5)


# In[32]:


sns.kdeplot(df['count'], shade=True)


# In[34]:


stop_and_search_df.groupby(["Type", "Gender", "year"])[['Self-defined ethnicity', 'Officer-defined ethnicity']].agg('count')


# In[70]:


df1 = stop_and_search_df.groupby(["Type", "Gender", "year"])['Self-defined ethnicity'].agg('count').to_frame(name = 'count').reset_index()


# In[71]:


df1.head()


# In[72]:


sns.boxplot(x="Type", y="count", hue="Gender", data=df1)


# In[74]:


sns.boxplot(x="year", y="count", hue="Gender", data=df1)


# In[50]:


stop_and_search_df.groupby(["Type", "Gender", "year", "Self-defined ethnicity", "Officer-defined ethnicity"])['Date'].agg('count')


# In[51]:


df2 = stop_and_search_df.groupby(["Type", "Gender", "year", "Self-defined ethnicity", "Officer-defined ethnicity"])['Date'].agg('count').to_frame(name = 'count').reset_index()


# In[52]:


df2.head()


# In[59]:


sns.set(rc={'figure.figsize':(15,15)})
sns.boxplot(x="Type", y="count", hue="Self-defined ethnicity", data=df2)


# In[83]:


sns.set(rc={'figure.figsize':(15,10)})
sns.boxplot(x="Type", y="count", hue="Officer-defined ethnicity", data=df2)


# In[61]:


sns.set(rc={'figure.figsize':(15,15)})
sns.boxplot(x="Gender", y="count", hue="Self-defined ethnicity", data=df2)


# In[82]:


sns.set(rc={'figure.figsize':(15,10)})
sns.boxplot(x="Gender", y="count", hue="Officer-defined ethnicity", data=df2)


# In[65]:


sns.set(rc={'figure.figsize':(8,8)})
sns.kdeplot(df2['count'], shade=True)


# In[75]:


sns.set(rc={'figure.figsize':(15,15)})
sns.boxplot(x="year", y="count", hue="Self-defined ethnicity", data=df2)


# In[81]:


sns.set(rc={'figure.figsize':(15,10)})
sns.boxplot(x="year", y="count", hue="Officer-defined ethnicity", data=df2)


# In[87]:


df2.dtypes


# In[92]:


df3 = df2[df2['count'] < 10000]


# In[93]:


sns.set(rc={'figure.figsize':(15,15)})
sns.boxplot(x="year", y="count", hue="Self-defined ethnicity", data=df3)


# In[95]:


sns.set(rc={'figure.figsize':(15,10)})
sns.boxplot(x="year", y="count", hue="Officer-defined ethnicity", data=df3)


# In[96]:


sns.set(rc={'figure.figsize':(15,15)})
sns.boxplot(x="Type", y="count", hue="Self-defined ethnicity", data=df3)


# In[97]:


sns.set(rc={'figure.figsize':(15,10)})
sns.boxplot(x="Type", y="count", hue="Officer-defined ethnicity", data=df3)


# In[ ]:




