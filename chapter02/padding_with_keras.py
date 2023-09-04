#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# In[6]:


preprocessed_sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]


# In[7]:


tokenizer = Tokenizer()
tokenizer.fit_on_texts(preprocessed_sentences)
encoded = tokenizer.texts_to_sequences(preprocessed_sentences)


# In[8]:


print(encoded)


# In[11]:


# 앞에 0 채우기
padded = pad_sequences(encoded)


# In[12]:


padded


# In[13]:


# 뒤에 0 채우기
padded = pad_sequences(encoded, padding='post')


# In[14]:


padded


# In[15]:


# 길이에 제한을 두고 패딩하기 (앞 단어 삭제)
padded = pad_sequences(encoded, padding='post', maxlen=5)


# In[16]:


padded


# In[17]:


# 길이에 제한을 두고 패딩하기 (뒷 단어 삭제)
padded = pad_sequences(encoded, padding='post', truncating='post', maxlen=5)


# In[18]:


padded


# In[19]:


# 다른 숫자로 패딩하기
last_value = len(tokenizer.word_index) + 1 # 단어 집합의 크기보다 1 큰 숫자를 사용
padded = pad_sequences(encoded, padding='post', value=last_value)


# In[20]:


padded


# In[ ]:




