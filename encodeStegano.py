#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


img = cv2.imread('input.png')


# In[3]:


cv2.imshow('input',img)
cv2.waitKey()
cv2.destroyAllWindows()


# In[4]:


height,width,channels = img.shape


# In[5]:


height,width,channels


# In[6]:


def splittobgr(val):
    b=(val&0xE0)>>5
    g=(val&0x1C)>>2
    r=(val&0x3)
    return ([b,g,r])


# In[7]:


msg="shell"
msglen = len(msg)


# In[8]:


bitlist=[]
for i in range(msglen):
    bitlist.append(splittobgr(ord(msg[i])))


# In[9]:


bitlist


# In[10]:


firstbit = splittobgr(msglen)


# In[11]:


firstbit


# In[12]:


def clearLSB3(val):
    return (val&0xF8)


# In[13]:


def encode(imgbit,msgbit):
    return (msgbit | clearLSB3(imgbit))


# In[14]:


for i in range(3):
    img[0,0][i]=encode(img[0,0][i],firstbit[i])


# In[15]:


c=0
f=0
for i in range(height):
    for j in range(1,width):
        if (c==msglen):
            f=1
            break
        for k in range(3):
            img[i,j][k]=encode(img[i,j][k],bitlist[c][k])
        print(img[i,j])
        c+=1
    if(f==1):
        break


# In[17]:


cv2.imwrite('output.png',img)


# In[ ]:




