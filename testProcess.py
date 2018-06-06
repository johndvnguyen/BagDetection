'''
Created on May 27, 2018

@author: Voko
'''
import cv2
import watershedProcess as wp
import superpixelProcess as spp

img = cv2.imread('images/bag1.png')
#print img.shape
cv2.imshow('Frame',img)
cv2.waitKey(0)
cv2.imshow('Frame', wp.watershedProcess(img))
cv2.waitKey(0)
 
# Crop image
#imCrop = img[y:y+h, x:x+w]
imCrop = img[100:400, 250:450]
#superPixel = spp.drawSlic(imCrop, 100)

cv2.imshow('Frame',imCrop)
cv2.waitKey(0) 
cv2.imshow('Frame',wp.watershedProcess(imCrop))
cv2.waitKey(0)

