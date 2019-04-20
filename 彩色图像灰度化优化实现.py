# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 09:29:10 2019

@author: Sean
"""

import cv2
import numpy as np


img = cv2.imread('yuan.bmp',1)
h = img.shape[0]
w = img.shape[1]

dst_gray = np.zeros((h,w,3),np.uint8)

for i in range(h):
    for j in range(w):
        b,g,r = img[i,j]
        #类型转换，uint8转换为int，不然速率太慢，不知为何
        b=int(b)
        g=int(g)
        r=int(r)
#        # r*0.299+g*0.587+b*0.114，处理速度较慢
#        gray = int(b*0.114 + g*0.587 + r*0.299)
        #等价于(b+g*2+r)/4，移位操作，比加减乘除都快
        gray = (b + (g<<1) + r)>>2
        dst_gray[i,j]=np.uint8(gray)

cv2.imshow('', dst_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
        