import cv2

img = cv2.imread('images/highway.jpg')

resize = cv2.resize(img, (520, 520))

kernel = 3
blur = cv2.medianBlur(resize, kernel)

cv2.imshow('Input', resize)
cv2.imshow('Output', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
