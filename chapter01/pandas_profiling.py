#!/usr/bin/env python
# coding: utf-8

# In[5]:


# spam.csv 가져오기
import pandas as pd
import pandas_profiling
data = pd.read_csv(r'C:\git\basic-nlp\chapter01\spam.csv',encoding='latin1')


# In[6]:


# 5개 행 출력하기
data[:5]


# In[7]:


# 프로파일링 리포트 생성
pr = data.profile_report()


# In[8]:


# 결과 보기
data.profile_report()


# In[9]:


pr


# In[ ]:




