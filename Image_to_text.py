import requests as rq
from textblob import TextBlob
import os
import pandas as pd
import pytesseract

from PIL import Image
album_raw = rq.get("https://images.gr-assets.com/quotes/1511992603p8/8630.jpg")   # random imageshttps://www.brainyquote.com/topics/random
with open("image.png",'wb') as raw_file:   
    raw_file.write(album_raw.content)

text=pytesseract.image_to_string(Image.open("image.png"))
print(text)
pos=0
neg=0
neutral=0
polarity=0
analysis="Good"
analysis=TextBlob(text)
polarity += analysis.sentiment.polarity
if(analysis.sentiment.polarity == 0):
    neutral+= 1
elif(analysis.sentiment.polarity <0.00):
    neg += 1
elif(analysis.sentiment.polarity>0.00):
    pos+=1
if(polarity==0):
 print("Neutral")
elif(polarity<0):
 print("Negative")
elif(polarity>0):
 print("Positive")
