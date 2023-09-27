#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv(r'C:\Users\saira\Downloads\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv', encoding= 'unicode_escape')


# In[3]:


df


# In[4]:


df.shape


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[8]:


df.shape


# In[9]:


df.head()


# In[10]:


pd.isnull(df).sum()


# In[11]:


df.dropna(inplace=True)


# In[12]:


pd.isnull(df).sum()


# In[13]:


df['Amount'].dtype


# In[14]:


df['Amount'].head(10)


# In[15]:


df['Amount']=df['Amount'].astype('int')


# In[16]:


df['Amount'].dtype


# In[17]:


df.columns


# In[18]:


df.rename(columns={'Marital_Status':'mstatus'},inplace=True)
df


# In[19]:


df[['Age','mstatus','Amount']].describe()


# In[20]:


df[['Age']].mean()


# In[21]:


df[['Age']].shape


# In[22]:


ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[23]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# In[24]:


df.sort_values(by='Age Group',ascending=True,inplace=True)
df


# In[25]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')


for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# In[27]:


sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[29]:


ax = sns.countplot(data = df, x = 'mstatus')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


sales_state = df.groupby(['mstatus', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'mstatus',y= 'Amount', hue='Gender')


# In[31]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# In[32]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[33]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# In[37]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[35]:


fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# In[ ]:




