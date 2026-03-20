import cv2

img = cv2.imread('images/highway.jpg')

rows = img.shape[0]
cols = img.shape[1]

center = (cols / 2, rows / 2)
angle = 180
scale = 1.0

r = cv2.getRotationMatrix2D(center, angle, scale)
rotate = cv2.warpAffine(img, r, (cols, rows))

cv2.imshow('Rotated', rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
