#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 정규 표현식을 사용한 단어 토큰화
from nltk.tokenize import RegexpTokenizer


# In[2]:


text = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop"


# In[7]:


# 문자 또는 숫자가 1개 이상인 경우를 토큰으로 규정
tokenizer1 = RegexpTokenizer("[\w]+")


# In[8]:


# 공백을 토큰으로 나누기 위한 기준으로 규정
# 'gaps=True' : 토큰을 나누기 위한 기준으로 사용한다는 의미
tokenizer2 = RegexpTokenizer("\s+", gaps=True)


# In[9]:


print(tokenizer1.tokenize(text))


# In[10]:


print(tokenizer2.tokenize(text))


# In[ ]:




