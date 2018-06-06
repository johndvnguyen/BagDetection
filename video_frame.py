import cv2
import os.path as Path
import numpy as np
import watershedProcess as wp

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
my_vid_file = './videos/AVSS_AB_Easy_Divx.avi'
#my_vid_file = './videos/AVSS_AB_Medium_Divx.avi'
print Path.isfile(my_vid_file)

cap = cv2.VideoCapture(my_vid_file)

# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

    # Display the resulting frame
        cv2.imshow('Frame',wp.watershedProcess(frame))
        #cv2.imshow('Frame',frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #if cv2.waitKey(1) & 0xFF == ord('p'):
    
    if cv2.waitKey(1) & 0xFF == ord('o'):
        wp.watershedProcess(frame)

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
