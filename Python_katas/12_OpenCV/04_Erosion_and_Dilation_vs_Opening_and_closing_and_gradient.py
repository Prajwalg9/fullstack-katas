import cv2
import numpy as np

image=cv2.imread("images/forest_image.png")
resized_image = cv2.resize(image,(800,600))
cv2.imshow("Original Image",resized_image)

kernel=np.ones((5,5),np.uint8)

# Erosion and Dilation:

# eroded_image = cv2.erode(resized_image,kernel,iterations = 1)
# cv2.imshow("Eroded Image",eroded_image)
#
# dilated_image = cv2.dilate(resized_image,kernel,iterations = 1)
# cv2.imshow("Dilated Image",dilated_image)


# Opening and closing

opened_image = cv2.morphologyEx(resized_image, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opened Image",opened_image)

closed_image=cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed Image",closed_image)

gradient_image=cv2.morphologyEx(resized_image,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("Gradient Image",gradient_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
