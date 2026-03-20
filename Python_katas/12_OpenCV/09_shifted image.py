import cv2
import numpy as np

img = cv2.imread('images/forest_image.png')

rows = img.shape[0]
cols = img.shape[1]

s = np.float32([[1, 0, 150],
                [0, 1, 70]])

shifted = cv2.warpAffine(img, s, (cols, rows))

cv2.imshow('Original Image', img)
cv2.imshow('Shifted Image', shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
