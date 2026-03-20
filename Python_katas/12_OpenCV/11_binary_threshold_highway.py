import cv2
import numpy as np

img = cv2.imread('images/highway.jpg', cv2.IMREAD_GRAYSCALE)

threshold_value = 100
max_value = 255

_, binary_threshold = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)

cv2.imshow('Original', img)
cv2.imshow('Binary Threshold', binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
