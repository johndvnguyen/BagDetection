import cv2
import numpy as np
import watershedProcess as wp

#bag_cascade = cv2.CascadeClassifier('')
person_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

cap = cv2.VideoCapture('AVSS_AB_Easy_Divx.avi')

while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #scalefactor is step for resizing reference (tradeoff accuracy(smaller) for speed (larger)
    #minNeighbors filters false positives (ie requries more neighboring frames to contain object)
    
#    bags = bag_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    people = person_cascade.detectMultiScale(gray, 1.2, 4)
    for (x, y, w, h) in people:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        wp.watershedProcess(frame[y:y+h, x:x+w])
        #cv2.imshow('Frame', wp.watershedProcess(frame[y:y+h, x:x+w]))
        #cv2.waitKey(0)
        
    cv2.imshow('orig', frame)
    if ret is False or (cv2.waitKey(1) & 0xff) == ord('q'): break
                      
cap.release()
cv2.destroyAllWindows()
