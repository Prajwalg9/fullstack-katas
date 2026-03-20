import cv2
import numpy as np

img = cv2.imread('images/highway.jpg', 0)
resize = cv2.resize(img, (520, 520))

min_thresh = 100
max_thresh = 200

edges = cv2.Canny(resize, min_thresh, max_thresh)

cv2.imshow('Original', resize)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
