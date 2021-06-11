#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:16:09 2021

@author: beryl
"""



import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from PIL import Image,ImageEnhance
import scipy.ndimage.filters as filters

#increase the contrast of tthe original image and save it
image = Image.open('ps205.jpg')
image_contr_obj = ImageEnhance.Contrast(image) #Contrast class instance
image_e = image_contr_obj.enhance(3)
data = np.array(image)
data_e = np.array(image_e)
plt.imsave('enhanced.jpg',data_e)

img = cv.imread('enhanced.jpg',0)
def halo_contour(img, lowthre, highthre, minR, maxR, mindist):
    img = cv.medianBlur(img,5)
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT, 1, mindist, param1=highthre, param2=lowthre, minRadius=minR, maxRadius=maxR)
    circles = np.uint16(np.around(circles))
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    for i in circles[0,:]:
        # draw the outer circle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)
        # draw the center of the circle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    plt.imshow(cimg)


# import cv2

# raw_image = cv2.imread('rawImage.jpg')
# cv2.imshow('Original Image', raw_image)
# cv2.waitKey(0)

# bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)
# cv2.imshow('Bilateral', bilateral_filtered_image)
# cv2.waitKey(0)

# edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
# cv2.imshow('Edge', edge_detected_image)
# cv2.waitKey(0)

# _, contours, hierarchy = cv.findContours(edge_detected_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# contour_list = []
# for contour in contours:
#     approx = cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
#     area = cv.contourArea(contour)
#     if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
#         contour_list.append(contour)

# cv2.drawContours(raw_image, contour_list,  -1, (255,0,0), 2)
# cv2.imshow('Objects Detected',raw_image)
# cv2.waitKey(0)

