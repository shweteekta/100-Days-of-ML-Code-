
# coding: utf-8

# In[52]:


import requests as rq


# In[3]:


get_ipython().system(u'wget -O skills.txt https://raw.githubusercontent.com/shweteekta/Datasets/master/skills.txt?token=AHRPPY4XUPUG5DTSMSDT5YK5A2DF4')


# In[4]:


data=open('skills.txt','r').read()


# In[5]:


get_ipython().system(u'pip install wordcloud')
from wordcloud import WordCloud, STOPWORDS


# In[6]:


stopwords = set(STOPWORDS)


# In[13]:


ds_wc = WordCloud(
    background_color='white',
    max_words=200,
    stopwords=stopwords
)

# generate the word cloud
ds_wc.generate(data)


# In[22]:


get_ipython().system(u'wget -O dsimage.png https://raw.githubusercontent.com/nikhilkumarsingh/wordcloud-example/master/cloud.png')


# In[23]:


import numpy as np
from PIL import Image
ds_mask = np.array(Image.open('dsimage.png'))
ds_mask


# In[24]:


import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_figwidth(10) # set width
fig.set_figheight(12) # set height

plt.imshow(ds_mask, cmap=plt.cm.gray)
plt.axis('off')
plt.show()


# In[33]:


ds_wc = WordCloud(background_color='white', max_words=3000, mask=ds_mask, stopwords=stopwords)
#stopwords=['practical','theoretical','across','strong','hands','demonstrated','etc']
# generatstope the word cloud
stopwords.add('econometric')
stopwords.add('CART')
stopwords.add('CAID')

ds_wc.generate(data)
fig=plt.figure(figsize=(13,8),facecolor = 'white', edgecolor='blue')
# display the word cloud
#fig = plt.figure()
fig.set_figwidth(13) # set width
fig.set_figheight(12) # set height

plt.imshow(ds_wc,interpolation="bilinear")
plt.axis('off')
plt.show()

