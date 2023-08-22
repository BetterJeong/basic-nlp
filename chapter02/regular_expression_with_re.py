#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[ ]:


# search() : 정규 표현식 전체에 대해 문자열이 매치하는지


# In[17]:


# '.' : 한 개의 임의의 문자
r = re.compile("a.c")


# In[18]:


r.search("kkk") # 결과가 출력되지 않음


# In[19]:


r.search("abc") # a.c 정규 표현식 패턴으로 매치


# In[20]:


# '?': ? 앞의 문자가 존재할 수도 있고 존재하지 않을 수도 있음
r = re.compile("ab?c")


# In[21]:


r.search("abbc") # 결과가 출력되지 않음


# In[22]:


r.search("abc") # b가 있는 것으로 판단하여 abc 매치


# In[23]:


r.search("ac") # b가 없는 것으로 판단하여 ac 매치


# In[24]:


# '*' : 바로 앞의 문자가 0개 이상일 경우
r = re.compile("ab*c")


# In[25]:


r. search("a")


# In[26]:


r.search("ac")


# In[27]:


r.search("abc")


# In[28]:


r.search("abbbbc")


# In[30]:


# '+' : *와 유사함, 앞의 문자가 최소 1개 이상이어야 함
r = re.compile("ab+c")


# In[31]:


r.search("ac")


# In[32]:


r.search("abc")


# In[33]:


r.search("abbbbc")


# In[34]:


# '^': 시작되는 문자열 지정
r = re.compile("^ab")


# In[35]:


r.search("bbc")


# In[36]:


r.search("zab")


# In[37]:


r.search("abz")


# In[39]:


# '{숫자}' : 문자에 해당 숫자를 붙인 만큼 반복한 것
r = re.compile("ab{2}c")


# In[40]:


r.search("ac")


# In[41]:


r.search("abc")


# In[42]:


r.search("abbbbbc")


# In[43]:


r.search("abbc")


# In[45]:


# '{숫자1, 숫자2}' : 해당 문자를 숫자1 이상 숫자 2이하만큼 반복한 것
r = re.compile("ab{2,8}c")


# In[46]:


r.search("ac")


# In[47]:


r.search("abc")


# In[48]:


r.search("abbbbbbbbbc")


# In[49]:


r.search("abbc")


# In[50]:


r.search("abbbbbbbbc")


# In[51]:


# '{숫자,}' : 해당 문자를 숫자 이상 반복
r = re.compile("a{2,}bc")


# In[52]:


r.search("bc")


# In[53]:


r.search("aa")


# In[54]:


r.search("aabc")


# In[55]:


r.search("aaaaaaaaabc")


# In[57]:


# '[]' : [] 안의 문자 중 한 개의 문자와 매치
r = re.compile("[abc]")


# In[58]:


r.search("zzz")


# In[59]:


r.search("a")


# In[60]:


r.search("aaaaaaa")


# In[61]:


r.search("baac")


# In[62]:


# 알파벳 소문자에 대해 범위 지정한 정규 표현식
r = re.compile("[a-z]")


# In[63]:


r.search("AAA")


# In[64]:


r.search("111")


# In[65]:


r.search("aBC")


# In[66]:


# '[^문자]' : ^뒤에 붙은 문자들 제외한 모든 문자 매치
r = re.compile("[^abc]")


# In[67]:


r.search("a")


# In[68]:


r.search("ab")


# In[69]:


r.search("b")


# In[70]:


r.search("d")


# In[71]:


r.search("1")


# In[72]:


# match() : 문자열의 첫 부분이 정규 표현식과 매치하는지 확인


# In[73]:


r = re.compile("ab.")


# In[74]:


r.match("kkkabc")


# In[75]:


r.search("kkkabc")


# In[76]:


r.search("abckkk")


# In[77]:


# split() : 입력된 정규 표현식 기준으로 문자열 분리, 리스트로 리턴


# In[78]:


text = "사과 딸기 수박 메론 바나나"


# In[79]:


# 공백 기준으로 분리
re.split(" ", text)


# In[80]:


text = """사과
딸기
수박
메론
바나나"""


# In[81]:


# 줄바꿈 기준으로 분리
re.split("\n", text)


# In[82]:


text = "사과+딸기+수박+메론+바나나"


# In[84]:


# + 기준으로 분리
re.split("\+", text)


# In[85]:


# findall() : 정규 표현식과 일치하는 모든 문자열을 리스트로 반환


# In[86]:


text = """이름 : 김철수
전화번호 : 010 - 1234 - 1234
나이 : 30
성별 : 남"""


# In[87]:


# 숫자를 의미하는 규칙으로 숫자만 찾아내기
re.findall("\d+", text)


# In[88]:


# 숫자가 없을 경우 빈 리스트 반환
re.findall("\d+", "문자열입니다.")


# In[89]:


# sub() : 정규 표현식 패턴과 일치하는 문자열을 다른 문자열로 대체
# 특수문자 제거하고 공백으로 처리하는 등의 용도로 사용
text = "Regular expression : A regular expression, regex or regexp[1] (sometimes called a rational expression)[2][3] is, in theoretical computer science and formal language theory, a sequence of characters that define a search pattern."


# In[90]:


preprocessed_text = re.sub('[^a-zA-Z]', ' ', text)


# In[91]:


print(preprocessed_text)


# In[93]:


# 정규 표현식을 활용한 텍스트 전처리


# In[94]:


text = """100 John    PROF
101 James   STUD
102 Mac   STUD"""


# In[95]:


# 최소 1개 이상의 공백인 패턴을 기준으로 분리
re.split('\s+', text)


# In[97]:


# 숫자만 찾기
re.findall('\d+', text)


# In[99]:


# 대문자만 찾기 (문자를 각각 가져옴)
re.findall('[A-Z]', text)


# In[100]:


# 대문자가 연속 네 번 등장하는 경우
re.findall('[A-Z]{4}', text)


# In[101]:


# 대문자로 구성된 문자열 찾기
re.findall('[A-Z][a-z]+', text)


# In[ ]:




