#!/usr/bin/env python
# coding: utf-8

# In[14]:


# NLTK를 사용한 품사 태깅
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


# In[15]:


text = "I am actively looking for Ph.D. students. and you are a Ph.D. student."


# In[16]:


tokenized_sentence = word_tokenize(text)


# In[17]:


print('단어 토큰화 :', tokenized_sentence)
print('품사 태깅 :', pos_tag(tokenized_sentence))


# In[23]:


pip install konlpy


# In[24]:


# KoNLPy를 사용한 한국어 형태소 토큰화
from konlpy.tag import Okt
from konlpy.tag import Kkma


# In[25]:


okt = Okt()
kkma = Kkma()


# In[26]:


# 형태소 추출
print('OKT 형태소 분석 :',okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))


# In[27]:


# 품사 태깅
print('OKT 품사 태깅 :',okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))


# In[28]:


# 명사 추출
print('OKT 명사 추출 :',okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요")) 


# In[ ]:




