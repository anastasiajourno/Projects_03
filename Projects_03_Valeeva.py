#!/usr/bin/env python
# coding: utf-8

# ## Project Week 3 Valeeva

# ## Houses in emergency condition in Sverdlovsk region, Russia

# In[7]:


import pandas as pd


# In[9]:


df = pd.read_csv("Alarm_Sverd_Clean.csv")


# In[17]:


#df.head()


# ### Total number of houses in emergency condition in the region

# In[16]:


len(df.index)


# There is a total of 3398 houses in emergency condition in Sverdlovsk region, which is right in the middle of Russia. Houses in emergency condition are those that ...  

# ### % of houses in the region that are in emergency condition

# In[19]:


round((len(df.index)/42210)*100)


# ### total number of people living in these conditions

# In[20]:


df.residents_count.sum()


# ### % of people in the region that live in emergency condition

# In[22]:


round(df.residents_count.sum()/4290067*100)


# In[25]:


df.info(verbose=True)


# In[28]:


df.determined_date.head()


# In[29]:


df.exploitation_start_year.head()


# In[32]:


#df.determined_date.str.split(pat="/")


# In[35]:


new = df.determined_date.str.split("/", n = 2, expand = True)


# In[37]:


new.head()


# In[39]:


df["determined_year"] = new[2]


# In[40]:


df.determined_year.head()


# In[46]:


df = df.dropna(subset=['determined_year'])


# In[47]:


df.determined_year = df.determined_year.astype(int)


# In[48]:


df['exploitation']=(df.determined_year-df.exploitation_start_year)


# ## On average, houses have been in use for 61 years before they are determined as emergency housing.

# In[52]:


df['exploitation'].median()


# ### there are, however, some outliers, such as the oldest house which is more than 200 years old...

# In[53]:


df['exploitation'].max()


# In[56]:


pd.set_option('display.max_columns', None)


# In[57]:


df.loc[df['exploitation'] == 204]


# ### or baby houses like this one which is just 1 year old but is already in emergency condition!

# In[54]:


df['exploitation'].min()


# In[ ]:


## Here is a distribution of the age of houses that are in emergency condition


# In[58]:


df['exploitation'].plot(kind='hist')


# ## As for the reason of the house being in emergency condition, it's mostly physical deterioration. However, fires are also a reason for 2% of the cases.

# In[59]:


df.alarm_reason.value_counts()


# In[60]:


round(df.alarm_reason.value_counts(normalize=True)*100)


# ## Resettlement

# In[61]:


df.planned_resettlement_date.head()


# In[62]:


df = df.dropna(subset=['planned_resettlement_date'])


# In[63]:


new = df.planned_resettlement_date.str.split("/", n = 2, expand = True)


# In[64]:


new.head()


# In[65]:


df["resettlement_year"] = new[2]


# In[67]:


df.resettlement_year.head()


# In[68]:


df.resettlement_year = df.resettlement_year.astype(int)


# In[69]:


df['wait_years']=(df.resettlement_year-df.determined_year)


# ## On average, people wait for the resettlement for 10 years

# In[70]:


df['wait_years'].median()


# In[74]:


#df.loc[df['alarm_reason'] == 'Пожар'].groupby(by="resettlement_year")


# In[86]:


df_fire = df[df['alarm_reason']=='Пожар']


# In[92]:


#ok so our of 29 houses that were on fire I only have 12 with the filled resettlement year
len(df_fire)


# In[ ]:


#we could use 0 as a replacement if this is not used throughout the dataset 


# ## And there are at least 6 houses that have been on fire but still waiting to be resettled!

# In[99]:


len(df_fire[df_fire['resettlement_year']>2021])

