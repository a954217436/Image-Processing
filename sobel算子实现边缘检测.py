# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 08:51:13 2019

@author: Sean
"""

import cv2
import numpy as np

img = cv2.imread('yuan.bmp')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = np.zeros(gray.shape, np.uint8)

for i in range(0, gray.shape[0] - 1):
    for j in range(0, gray.shape[1] - 1):
        #sobel算子，[[1 2 1],[0 0 0],[-1 -2 -1]]
        #sobel算子，[[1 0 -1],[2 0 -2],[1 0 -1]]
        gx = gray[i-1, j-1] + 2 * gray[i-1, j] + gray[i-1, j+1] - \
             gray[i+1, j-1] - 2 * gray[i+1, j] - gray[i+1, j+1]
             
        gy = gray[i-1, j-1] + 2 * gray[i, j-1] + gray[i+1, j-1] - \
             gray[i-1, j+1] - 2 * gray[i, j+1] - gray[i+1, j+1]
        
        grad = np.sqrt(gx*gx + gy*gy)
        if grad > 50:
            dst[i, j] = 255

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


