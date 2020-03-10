# -*- coding: utf-8 -*-
# USAGE
# python opencv_object_tracking.py
# python opencv_object_tracking.py --video dashcam_boston.mp4 --tracker csrt
# Press `s` key to begin tracking
# CREDITS: https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
import numpy as np



cap = cv2.VideoCapture("video1.mp4")

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


while True:
        r, img = cap.read()
        #img=cv2.rotate(img,0 ) -----> para o video 2

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        minimo= np.array([225, 225, 225])
        maximo=np.array([255, 255, 255])
        mask = cv2.inRange(img_rgb, minimo, maximo)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        final = cv2.bitwise_and(img, img, mask=mask)
        bordas = auto_canny(final)

        

        lines = cv2.HoughLinesP(bordas, 1, np.pi/180, 100,None, 100, 30)   
        m1=[]
        m2=[]
        ponto1=[]
        ponto2=[]
        if lines is not None:
            for i in range(0, len(lines)):
                l = lines[i][0]
                m=(l[3]-l[1])/(l[2]-l[0])
                if m> -2.71 and m<-0.70:
                  m1.append(m)
                  ponto1.append(l)
                elif m>0.56 and m<2.03:
                  m2.append(m)
                  ponto2.append(l)

                print("ponto1", ponto1)
                print("ponto2", ponto2)
                if len(ponto1) <1 or len(ponto2) < 1:
                  continue
                h1=ponto1[0][1]-(m1[0]*ponto1[0][0])
                h2=ponto2[0][1]-(m2[0]*ponto2[0][0])
                
                x0=int((h2-h1)/(m1[0]-m2[0]))
                y0=int(m1[0]*x0+h1)


                print("PF", x0,y0)
                cv2.line(final, (l[0], l[1]), (x0, y0), (0,0,255), 3, cv2.LINE_AA)
                cv2.circle(final,(x0,y0),10,(255,255,0),4)

   
        cv2.imshow("edges", final)
      

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break     

