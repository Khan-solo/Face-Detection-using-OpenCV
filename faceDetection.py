# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:38:05 2018

@author: Mursil
"""

import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")

gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray_img,
                                     scaleFactor=1.05,
                                     minNeighbors=5)

print(face)


for x,y,w,h in face:
    img=cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0), 3)


cv2.imshow("Face Detected!",img)
cv2.waitKey(0)
cv2.destroyAllWindows()