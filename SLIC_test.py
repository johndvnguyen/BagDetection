'''
Created on May 27, 2018

@author: Voko
'''
import numpy
import cv2


images = []
img = cv2.imread('water_coins.jpg')
cv2.imshow('intitial_image' , img)

cv2.ximgproc.createSuperpixelSLIC(img)