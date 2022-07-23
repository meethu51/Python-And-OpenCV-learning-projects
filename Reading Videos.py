#Reading Videos
import cv2 as cv

capture = cv.VideoCapture('Videos/DOG.mp4') 

while True: #inside this while loop we grab the video frame by frame by using capture.read method
    isTrue, frame = capture.read()
    cv.imshow('Video',frame) #display using cv.imshow

    if cv.waitKey(20) & 0xFF == ord('d'): #if letter d is pressed break out of loop and stop displaying video or else windows will keep popping up to display the video
        break

capture.release
cv.destroyAllWindows() #destroys the window since we dont need it anymore