import cv2

img = cv2.imread('images/highway.jpg')

resize = cv2.resize(img, (520, 520))

d = 7
sigmacolor = 100
sigmaspace = 100

b = cv2.bilateralFilter(resize, d, sigmacolor, sigmaspace)

cv2.imshow('Input', resize)
cv2.imshow('Output', b)

cv2.waitKey(0)
cv2.destroyAllWindows()
