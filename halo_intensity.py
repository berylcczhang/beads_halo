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

#increase the contrast of tthe original image and save it
raw_image = Image.open('Tube5_1.tif')
RGB_image = raw_image.convert('RGB')
image_contr_obj = ImageEnhance.Contrast(RGB_image) #Contrast class instance
RGB_image_e = image_contr_obj.enhance(3)
data = np.array(RGB_image)
data_e = np.array(RGB_image_e )
plt.imsave('enhanced.jpg',data_e)

# #edge detection
# image_e = 


# data_max = filters.maximum_filter(data,1)
# data_min = filters.minimum_filter(data,5)
# maxima = (data_max == data)
# diff = ((data_max-data_min)>15)
# maxima[diff==0] = 0
# plt.imshow(maxima, cmap='gray', vmin=0,vmax=0.1)
# plt.imsave('maxima.jpg', maxima)


# img = cv.imread()




# maxima = cv.imread('maxima.jpg')
# output = maxima.copy()
# img = cv.cvtColor(maxima, cv.COLOR_BGR2GRAY)
# # Find circles
# circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1.3, 100)
# # If some circle is found
# if circles is not None:
#     # Get the (x, y, r) as integers
#     circles = np.round(circles[0, :]).astype("int")
#     print(circles)
#     # loop over the circles
#     for (x, y, r) in circles:
#       cv.circle(output, (x, y), r, (0, 255, 0), 2)
# # show the output image
# cv.imshow("circle",output)

# # Find circle
