#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

img = cv2.imread('input.png')

'''
cv2.imshow('input',img)
cv2.waitKey()
cv2.destroyAllWindows()
'''

height,width,channels = img.shape

height,width,channels

def splitToBgr(val):
    b=(val&0xE0)>>5
    g=(val&0x1C)>>2
    r=(val&0x3)
    return ([b,g,r])

def encrypt(msg,password):
    msgList = list(msg)
    pswdList = list(password)
    msglen = len(msgList)
    pswdlen = len(pswdList)

    pswdPos = 0
    for i in range(msglen):
        if(pswdPos==len(pswdList)):
            pswdPos=0
        msgList[i]= chr(ord(msgList[i])+ord(pswdList[pswdPos]))
        pswdPos+=1

    return (''.join(msgList))

msg=input('Enter your message:')
msglen = len(msg)
password = input('Enter password:')

msg = encrypt(msg,password)
print(f'your encrypted msg is: {msg}')

bitlist=[]
for i in range(msglen):
    bitlist.append(splitToBgr(ord(msg[i])))

firstbit = splitToBgr(msglen)

def clearLSB3(val):
    return (val&0xF8)

def encode(imgbit,msgbit):
    return (msgbit | clearLSB3(imgbit))

for i in range(3):
    img[0,0][i]=encode(img[0,0][i],firstbit[i])

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

cv2.imwrite('output.png',img)
