
# coding: utf-8

# In[6]:


import pandas as pd
get_ipython().system(u'ls')


# In[1]:


from sklearn import datasets


# In[3]:


digits=datasets.load_digits()


# In[4]:


print(digits)


# In[5]:


features=digits.data
labels=digits.target
print(features,labels)


# In[6]:


from sklearn import tree,preprocessing
from sklearn.model_selection import train_test_split 
from sklearn import metrics


# In[7]:


X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=1)


# In[8]:


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)


# In[9]:


y_pred1 =  clf.predict(X_test)


# In[10]:


metrics.accuracy_score(y_test, y_pred1)


# In[11]:


from scipy import misc


# In[14]:


from IPython.display import Image as IPythonImage
from PIL import Image
import requests as rq


# In[31]:


album_raw = rq.get("https://raw.githubusercontent.com/arneec/digits-recognition/master/5.jpg")   # random images
with open("image.jpg",'wb') as raw_file:   #widthbairer 
    raw_file.write(album_raw.content)


# In[32]:


img = Image.open("image.jpg")
IPythonImage(filename= 'image.jpg')   #To display the image


# In[33]:


img=misc.imread("image.jpg")


# In[34]:


print(features.shape)


# In[35]:


img=misc.imresize(img,(8,8))


# In[36]:


img=img.astype(digits.images.dtype)
img=misc.bytescale(img,high=16,low=0)


# In[40]:


y_pred=[]


# In[41]:


for eachrow in img:
    for eachpixel in eachrow:
        y_pred.append(sum(eachpixel)/3.0)
        


# In[42]:


print(clf.predict([x_test]))

