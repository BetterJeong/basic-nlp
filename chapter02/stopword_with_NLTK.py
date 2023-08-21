#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt


# In[9]:


# 불용어 확인하기
stop_words_list = stopwords.words('english')    # NLTK에 정의되어 있는 불용어 리스트
print('불용어 개수: ', len(stop_words_list))
print('불용어 10개 출력: ', stop_words_list[:10])


# In[11]:


# 불용어 제거를 위한 예시
example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english'))


# In[12]:


# 토큰화
word_tokens = word_tokenize(example)


# In[13]:


# 불용어 제거
result = []
for word in word_tokens:
    if word not in stop_words:
        result.append(word)


# In[14]:


print('불용어 제거 전: ', word_tokens)
print('불용어 제거 후: ', result)


# In[15]:


okt = Okt()


# In[16]:


# 한국어 불용어 제거를 위한 샘플
example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."


# In[17]:


# 불용어 정의
stop_words = "를 아무렇게나 구 우려 고 안 돼 같은 게 구울 때 는"


# In[18]:


# 토큰화
stop_word = set(stop_words.split(' '))
word_tokens = okt.morphs(example)


# In[21]:


# 불용어 제거
result = [word for word in word_tokens if not word in stop_words]


# In[22]:


print('불용어 제거 전: ', word_tokens)
print('불용어 제거 후: ', result)


# In[23]:


# 한국어 불용어 리스트: https://www.ranks.nl/stopwords/korean


# In[ ]:




