#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer


# In[2]:


preprocessed_sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]


# In[3]:


tokenizer = Tokenizer()
tokenizer.fit_on_texts(preprocessed_sentences)


# In[4]:


encoded = tokenizer.texts_to_sequences(preprocessed_sentences)


# In[5]:


print(encoded)


# In[6]:


max_len = max(len(item) for item in encoded)


# In[7]:


print('최대 길이 :', max_len)


# In[8]:


# 최대 길이인 7로 문장 길이 맞추기


# In[13]:


# 길이가 7보다 짧은 문장의 경우 숫자 0을 붙임
for sentence in encoded:
    while len(sentence) < max_len:
        sentence.append(0)
        
padded_np = np.array(encoded)


# In[14]:


padded_np


# In[ ]:




