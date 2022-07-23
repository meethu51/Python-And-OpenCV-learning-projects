from typing import Text
import cv2 as cv
import numpy as np

#there are 2 ways to draw on images 
#1.draw on standalone image
#2.draw on dummy image
#lets do no2.

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank) # this is the blank image you can draw on

#1.paint the image a certain color
blank[200:300, 300:400]= 208,224,64 #u can also color a certain portion of the image by giving it a range of pixels. eg blank[200:300, 300:400]
cv.imshow('Green',blank)

#2.drawing a rectangle

cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=2) #how to fill the entire rectangle? replace thickness=2 with thickness=cv.FILLED or -1
cv.imshow('Rectangle',blank)

#3.drawing a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)  

#4.Draw a line
cv.line(blank,(0,0),(300,400),(255,255,255),thickness=3)
cv.imshow('line',blank)

#5.Write Text
cv.putText(blank,'Hello My name is Bhuvan',(0,225),cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0), thickness=2)
cv.imshow('Text',blank) #Change the margin to fit text
#img = cv.imread('Photos/Cuiwen 2.jpeg') # this is the Chosen Image that you want to draw on
#cv.imshow('Cuiwen 2',img)

cv.waitKey(0)