# source: https://opencv.org/get-started/

import cv2 as cv
img = cv.imread('blobs.png')

cv.imshow("blobs png from Fiji builtins", img)
k = cv.waitKey(0) # Wait for a keystroke in the window (entering 1 would automatically close the window)