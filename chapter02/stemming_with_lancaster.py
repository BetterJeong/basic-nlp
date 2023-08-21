#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


# In[2]:


porter_stemmer = PorterStemmer()
lancaster_stemmer = LancasterStemmer()


# In[3]:


words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']


# In[4]:


print('어간 추출 전 :', words)


# In[5]:


print('포터 스테머의 어간 추출 후: ', [porter_stemmer.stem(w) for w in words])
print('랭커스터 스테머의 어간 추출 후: ', [lancaster_stemmer.stem(w) for w in words])


# In[ ]:




