import numpy as np
import cv2
from matplotlib import pyplot as plt

images = []
img = cv2.imread('water_coins.jpg')
cv2.imshow('intitial_image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#images.append(('gray',gray))
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#images.append(('thresh',thresh))


# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
#images.append(('sure_bg',sure_bg))

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
#images.append(('sure_fg',sure_fg))
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
#images.append(('unknown_area', unknown))

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0
#images.append(('markers',markers))

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
#images.append(('markers', markers))
images.append(('final', img))

#retval	=	cv.ximgproc.createSuperpixelSLIC(	image[, algorithm[, region_size[, ruler]]]	)



for x in range(0,len(images)):
    cv2.imshow(images[x][0] ,images[x][1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
