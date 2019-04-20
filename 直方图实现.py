# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 09:50:12 2019

@author: Sean
"""

import cv2
import numpy as np


def imgHist(img):    
    height = img.shape[0]
    width = img.shape[1]
    
    b_list = np.zeros([256], np.uint8)
    g_list = np.zeros([256], np.uint8)
    r_list = np.zeros([256], np.uint8)
    
    for i in range(0,height):
        for j in range(0,width):
            b_index,g_index,r_index = img[i,j]
            b_index = int(b_index)
            g_index = int(g_index)
            r_index = int(r_index)
            
            b_list[b_index] += 1
            g_list[g_index] += 1
            r_list[r_index] += 1
    
#    for i in range(256):
#        b_list[i] = b_list[i] / (height*width)
#        g_list[i] = g_list[i] / (height*width)
#        r_list[i] = r_list[i] / (height*width)
    
    cv2.namedWindow('B_Hist')
    cv2.namedWindow('G_Hist')
    cv2.namedWindow('R_Hist')
    
    b_dst = np.zeros((256,256,3), np.uint8)
    g_dst = np.zeros((256,256,3), np.uint8)
    r_dst = np.zeros((256,256,3), np.uint8)
    
    for i in range(256):
        cv2.line(b_dst, (i, 256-b_list[i]), (i,256), (255,0,0), 2, cv2.LINE_AA)
        cv2.line(g_dst, (i, 256-g_list[i]), (i,256), (0,255,0), 2, cv2.LINE_AA)
        cv2.line(r_dst, (i, 256-r_list[i]), (i,256), (0,0,255), 2, cv2.LINE_AA)
    
    cv2.imshow('B_Hist', b_dst)
    cv2.imshow('G_Hist', g_dst)
    cv2.imshow('R_Hist', r_dst)
    
    
    
img = cv2.imread('DLAM.jpg')
imgHist(img)
cv2.waitKey(0)
cv2.destroyAllWindows()