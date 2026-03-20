import cv2
import numpy as np

image=cv2.imread("images/forest_image.png")
cv2.imshow("Forest Image",image)

kernel = np.ones((5,5),np.uint8)

tophat_image= cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)
cv2.imshow("Tophat Image",tophat_image)

Blackhat_image = cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("Blackhat Image",Blackhat_image)

cv2.waitKey(0)

cv2.destroyAllWindows()