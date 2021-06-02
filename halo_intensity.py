#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:30:33 2021

@author: beryl
"""



import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from PIL import Image,ImageEnhance
import scipy.ndimage.filters as filters

#enhanced method: increase the contrast of the original image and save it
raw_image = Image.open('Tube5_1.tif')
RGB_image = raw_image.convert('RGB')
image_contr_obj = ImageEnhance.Contrast(RGB_image) #Contrast class instance
RGB_image_e = image_contr_obj.enhance(3)
RGB_data_e = np.array(RGB_image_e)
plt.imsave('enhanced.jpg',RGB_data_e)



#filter method 
def get_maxima(max_nbsize, min_nbsize, threshold):
    data = np.array(raw_image)
    data_max = filters.maximum_filter(data,max_nbsize)
    data_min = filters.minimum_filter(data,min_nbsize)
    maxima = (data_max == data)
    diff = ((data_max-data_min)>threshold)
    maxima[diff==0] = 0
    plt.imshow(maxima, cmap='gray', vmin=0,vmax=0.1)
    plt.imsave('maxima.jpg', maxima)

#edge detect for enhanced method
img = cv.imread('enhanced.jpg',0)
def halo_contour(img, lowthre, highthre, minR, maxR, mindist):
    img = cv.medianBlur(img,5)
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT, 1, mindist, param1=highthre, param2=lowthre, minRadius=minR, maxRadius=maxR)
    circles = np.uint16(np.around(circles))
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    for i in circles[0,:]:
        # draw the outer circle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    plt.imshow(cimg)
    
    
# # edge detect for filter method

# img = cv.imread('maxima.jpg',0)
# # img = cv.medianBlur(img,5)
# edge = cv.Canny(img,170,200)
# cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
# circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
# circles = circles = np.uint16(np.around(circles))

# for i in circles[0,:]:
#     # draw the outer circle
#     cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

# plt.imshow(cimg)

