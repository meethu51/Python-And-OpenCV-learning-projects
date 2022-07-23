import cv2 as cv

# We usually resize and rescale images and video files to prevent computational strain
# large media files take a lot of processing power meaning slower loading and etc
# we r trying to get rid of this computation strain by modifying the medias dimensions

#Resizing image


img = cv.imread('Photos/Cuiwen 2.jpeg')

cv.imshow('Cuiwen 2', img)

def rescaleFrame(frame, scale = 0.5): #function to rescale the provided media above
    #this method works for images videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA) #it resizes the frame to a particular dimension
resized_image = rescaleFrame(img)
cv.imshow('image', resized_image)

######################################################

#Resizing Videos

#how to resize video frames specifically?using capture.set method

#only live videos only
#def changeRes(width,height):
    #capture.set(3,width)
    #capture.set(4,height)


capture = cv.VideoCapture('Videos/DOG.mp4') 

while True: 
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=0.2)#function to rescale the provided media above

    cv.imshow('Video',frame) 
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'): 
        break

capture.release
cv.destroyAllWindows()



