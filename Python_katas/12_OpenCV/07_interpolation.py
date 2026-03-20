import cv2

image = cv2.imread("images/forest_image.png")
cv2.imshow("Original", image)

print("Dimensions of original image:", image.shape)

scale = 0.5
width = int(image.shape[1] * scale)
height = int(image.shape[0] * scale)
dimensions = (width, height)

inter_area = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)
cv2.imshow("Inter Area", inter_area)

inter_cubic = cv2.resize(image, dimensions, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Inter Cubic", inter_cubic)

cv2.waitKey(0)
cv2.destroyAllWindows()