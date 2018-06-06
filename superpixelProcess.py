'''
Created on Jun 5, 2018

@author: Voko
'''
# had to run: 
#pip install -U scikit-image
#pip install -U scipy
# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import cv2
import matplotlib.pyplot as plt

def drawSlic(image,numSegments):
    segments = slic(image, n_segments = numSegments, sigma = 5)
 
    # show the output of SLIC
    fig = plt.figure("Superpixels -- %d segments" % (numSegments))
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(mark_boundaries(image, segments))
    plt.axis("off")
    plt.show()

def sppMain():
    # load the image and convert it to a floating point data type
    image = img_as_float(cv2.imread('images/bag1.png'))
     
    # loop over the number of segments
    for numSegments in (300, 500, 1000):
        # apply SLIC and extract (approximately) the supplied number
        # of segments
        segments = slic(image, n_segments = numSegments, sigma = 5)
     
        # show the output of SLIC
        fig = plt.figure("Superpixels -- %d segments" % (numSegments))
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(mark_boundaries(image, segments))
        plt.axis("off")
     
    # show the plots
    plt.show()