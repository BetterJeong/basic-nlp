#!/usr/bin/env python
# coding: utf-8

# In[7]:


import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer


# In[8]:


lemmatizer = WordNetLemmatizer()


# In[9]:


words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']


# In[12]:


print('표제어 추출 전: ', words)
print('표제어 추출 후: ', [lemmatizer.lemmatize(word) for word in words])


# In[11]:


lemmatizer.lemmatize('dies', 'v')


# In[13]:


lemmatizer.lemmatize('watched', 'v')


# In[14]:


lemmatizer.lemmatize('has', 'v')


# In[ ]:




