#!/usr/bin/env python
# coding: utf-8

import cv2

img = cv2.imread('output.png')

'''
cv2.imshow('input',img)
cv2.waitKey()
cv2.destroyAllWindows()
'''

height,width,channels = img.shape

def jointomsg(imgbit):
    ans = ((imgbit[0]&7)<<5)|((imgbit[1]&7)<<2)|(imgbit[2]&3)
    return ans

msglen = jointomsg(img[0,0])

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

print(msg)
