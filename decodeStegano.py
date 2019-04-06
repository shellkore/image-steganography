#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


img = cv2.imread('output.png')


# In[3]:


cv2.imshow('input',img)
cv2.waitKey()
cv2.destroyAllWindows()


# In[4]:


height,width,channels = img.shape


# In[5]:


height,width,channels


# In[6]:


def jointomsg(imgbit):
    ans = ((imgbit[0]&7)<<5)|((imgbit[1]&7)<<2)|(imgbit[2]&3)
    return ans


# In[7]:


msglen = jointomsg(img[0,0])


# In[8]:


c=0
f=0
msg=''
for i in range(height):
    for j in range(1,width):
        if(c==msglen):
            f=1
            break
        msg+=chr(jointomsg(img[i,j]))
        c+=1
    if(f==1):
        break


# In[9]:


print(msg)


# In[ ]:




