#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# In[2]:


raw_text = "A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."


# In[3]:


# 문장 토큰화
sentences = sent_tokenize(raw_text)
print(sentences)


# In[4]:


vocab = {}
preprocessed_sentences = []
stop_words = set(stopwords.words('english'))


# In[5]:


for sentence in sentences:
    # 단어 토큰화
    tokenized_sentence = word_tokenize(sentence)
    result = []

    for word in tokenized_sentence: 
        word = word.lower() # 모든 단어를 소문자화
        if word not in stop_words: # 단어 토큰화 된 결과에 대해 불용어 제거
            if len(word) > 2: # 단어 길이가 2이하인 경우에 대해 추가로 단어 제거
                result.append(word)
                if word not in vocab:
                    vocab[word] = 0 
                vocab[word] += 1
    preprocessed_sentences.append(result)


# In[6]:


print(preprocessed_sentences)


# In[7]:


print('단어 집합 :',vocab)


# In[8]:


print(vocab["barber"])


# In[9]:


vocab_sorted = sorted(vocab.items(), key = lambda x:x[1], reverse = True)
print(vocab_sorted)


# In[10]:


word_to_index = {}
i = 0


# In[11]:


for (word, frequency) in vocab_sorted :
    if frequency > 1 : # 빈도수가 작은 단어는 제외.
        i = i + 1
        word_to_index[word] = i


# In[12]:


print(word_to_index)


# In[13]:


vocab_size = 5


# In[14]:


words_frequency = [word for word, index in word_to_index.items() if index >= vocab_size + 1]


# In[15]:


for w in words_frequency:
    del word_to_index[w]


# In[16]:


print(word_to_index)


# In[17]:


word_to_index['OOV'] = len(word_to_index) + 1


# In[18]:


print(word_to_index)


# In[19]:


encoded_sentences = []


# In[20]:


for sentence in preprocessed_sentences:
    encoded_sentence = []
    for word in sentence:
        try:
            # 단어 집합에 있는 단어라면 해당 단어의 정수를 리턴.
            encoded_sentence.append(word_to_index[word])
        except KeyError:
            # 만약 단어 집합에 없는 단어라면 'OOV'의 정수를 리턴.
            encoded_sentence.append(word_to_index['OOV'])
    encoded_sentences.append(encoded_sentence)


# In[21]:


print(encoded_sentences)


# In[22]:


from collections import Counter


# In[23]:


print(preprocessed_sentences)


# In[24]:


# words = np.hstack(preprocessed_sentences)으로도 수행 가능.
all_words_list = sum(preprocessed_sentences, [])
print(all_words_list)


# In[25]:


vocab = Counter(all_words_list)
print(vocab)


# In[26]:


print(vocab["barber"])


# In[27]:


vocab_size = 5


# In[28]:


vocab = vocab.most_common(vocab_size)


# In[29]:


word_to_index = {}
i = 0


# In[30]:


for (word, frequency) in vocab :
    i = i + 1
    word_to_index[word] = i


# In[31]:


print(word_to_index)


# In[32]:


from nltk import FreqDist
import numpy as np


# In[33]:


vocab = FreqDist(np.hstack(preprocessed_sentences))


# In[34]:


print(vocab["barber"])


# In[35]:


vocab_size = 5
vocab = vocab.most_common(vocab_size)


# In[36]:


word_to_index = {word[0] : index + 1 for index, word in enumerate(vocab)}


# In[37]:


print(word_to_index)


# In[38]:


test_input = ['a', 'b', 'c', 'd', 'e']


# In[39]:


for index, value in enumerate(test_input):
  print("value : {}, index: {}".format(value, index))


# In[40]:


from tensorflow.keras.preprocessing.text import Tokenizer


# In[41]:


preprocessed_sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]


# In[42]:


tokenizer = Tokenizer()


# In[43]:


tokenizer.fit_on_texts(preprocessed_sentences) 


# In[44]:


print(tokenizer.word_index)


# In[45]:


print(tokenizer.word_counts)


# In[46]:


print(tokenizer.texts_to_sequences(preprocessed_sentences))


# In[47]:


vocab_size = 5


# In[48]:


tokenizer = Tokenizer(num_words = vocab_size + 1)
tokenizer.fit_on_texts(preprocessed_sentences)


# In[49]:


print(tokenizer.word_index)


# In[50]:


print(tokenizer.word_counts)


# In[51]:


print(tokenizer.texts_to_sequences(preprocessed_sentences))


# In[52]:


tokenizer = Tokenizer()
tokenizer.fit_on_texts(preprocessed_sentences)


# In[53]:


vocab_size = 5
words_frequency = [word for word, index in tokenizer.word_index.items() if index >= vocab_size + 1] 


# In[54]:


for word in words_frequency:
    del tokenizer.word_index[word]
    del tokenizer.word_counts[word]


# In[55]:


print(tokenizer.word_index)
print(tokenizer.word_counts)
print(tokenizer.texts_to_sequences(preprocessed_sentences))


# In[56]:


vocab_size = 5
tokenizer = Tokenizer(num_words = vocab_size + 2, oov_token = 'OOV')
tokenizer.fit_on_texts(preprocessed_sentences)


# In[57]:


print('단어 OOV의 인덱스 : {}'.format(tokenizer.word_index['OOV']))


# In[58]:


print(tokenizer.texts_to_sequences(preprocessed_sentences))


# In[ ]:




