#!/usr/bin/env python
# coding: utf-8

# In[114]:



import pandas as pd


# In[115]:


df=pd.read_csv('data/info.csv',sep='|',index_col='user_id')
df


# In[37]:


print(df.head(10))
print(df.tail(10))


# In[40]:


df.shape[0]


# In[41]:


df.shape[1]


# In[46]:


df.columns


# In[47]:


df.index


# In[71]:


print(type(df))
print(df.dtypes)


# In[72]:


df.occupation


# In[74]:


len(df.occupation.unique())


# In[111]:


df.occupation.value_counts().head().index[0]


# In[112]:


df.info(verbose=True)


# In[83]:


df.describe()


# In[85]:


df.describe(include = 'all' )


# In[91]:


df.occupation.describe()


# In[96]:


df.age.mean()


# In[113]:


df.age.value_counts().tail()


# In[ ]:




