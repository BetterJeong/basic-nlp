#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


# In[2]:


stemmer = PorterStemmer()


# In[3]:


sentence = "This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."


# In[4]:


tokenized_sentence = word_tokenize(sentence)


# In[8]:


print('어간 추출 전: ', tokenized_sentence)
print('어간 추출 후: ', [stemmer.stem(word) for word in tokenized_sentence])


# In[9]:


words = ['formalize', 'allowance', 'electricical']


# In[10]:


print('어간 추출 전 :',words)
print('어간 추출 후 :',[stemmer.stem(word) for word in words])


# In[ ]:




