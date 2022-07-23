import cv2 as cv

img = cv.imread('Photos/Cuiwen 2.jpeg')

cv.imshow("Cuiwen 2",img)

# Converting an image to Grayscale (Function1)[Converts image to gray to see intensity]
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray',gray)

# How to blurr an image
blur =cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT) # the (3,3) is the blur intensity so if u want more blur increase the number BUT THE NUMBER MUST ALWAYS BE ODD!!
cv.imshow('Blur',blur)

# Edge Cascade [This shows the edges][If u want to reduce the edges pass in the blur variable instead of img]note:More blur= less edges(inversely proportional)
canny = cv.Canny(img, 125,175)
cv.imshow('Canny Edges',canny)

# How to Dilate an image using a specific structuring element
dilated = cv.dilate(canny,(7,7), iterations=4) #increasing iterations will increase thickness and kernel size controls the dilation
cv.imshow('Dilated',dilated)

# How to Erode an image
eroded = cv.erode(dilated)
cv.waitKey(0)