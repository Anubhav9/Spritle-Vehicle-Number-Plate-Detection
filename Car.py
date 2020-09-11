#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


import cv2
import imutils


# In[4]:


img=cv2.imread('trial.jpg')


# In[5]:


##printing the image


# In[6]:


cv2.imshow("original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[7]:


##converting image from bgr to black and white


# In[8]:


img_cvt=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# In[9]:


##printing gray scale image
cv2.imshow("gray image",img_cvt)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


##bilateral filter to remove the noise
img_new=cv2.bilateralFilter(img_cvt,10,10,10)


# In[11]:


##printing bilateral filtered image
cv2.imshow("Bilateral Filter Image",img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


##performing canny edge detection to detect the edges


# In[13]:


img_new=cv2.Canny(img_new,150,200)


# In[14]:


##result after canny edge detection
cv2.imshow("Canny Edge Detection Result",img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[15]:


##detecting the license plate which has 4 edges
cnt = cv2.findContours(img_new.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = imutils.grab_contours(cnt)
cnt=sorted(cnt, key = cv2.contourArea, reverse = True)[:20] 
PlateDetected = None 

count = 0
for c in cnt:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.03 * perimeter, True)
        if len(approx) == 4:  # Select the contour with 4 corners
            PlateDetected = approx #This is our approx Number Plate Contour
            break


# In[16]:


PlateDetected


# In[17]:


mask = np.zeros(img_cvt.shape,np.uint8)
img_latest=cv2.drawContours(mask,[PlateDetected],0,255,-1)


# In[18]:


##bitwise and the image to onlt get the required part of the image
new_image = cv2.bitwise_and(img,img,mask=mask)


# In[19]:


cv2.imshow("result",new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[20]:


(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = img_cvt[topx:bottomx+1, topy:bottomy+1]


# In[32]:


##Cropped=cv2.resize(Cropped,(600,600))


# In[21]:


cv2.imshow("result",Cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[22]:


import pytesseract


# In[23]:


text = pytesseract.image_to_string(Cropped,config='--psm 11')


# In[28]:


for i in range(0,13):
    print(text[i],end="")


# In[ ]:




