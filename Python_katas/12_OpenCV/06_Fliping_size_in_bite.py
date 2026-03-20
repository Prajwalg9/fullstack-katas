import cv2

image=cv2.imread("images/forest_image.png")
cv2.imshow("Original Image",image)

# Fliping Images>>

# 1 Horizontal Flip:
Horizontal_Flip=cv2.flip(image,1)
cv2.imshow("Horizontal Flip",Horizontal_Flip)

# 2. Vertical Flip:
Vertical_Flip=cv2.flip(image,0)
cv2.imshow("Vertical Flip",Vertical_Flip)

# 3. Horizontal + vertical Flip:
Horizontal_vertical=cv2.flip(image,-1)
cv2.imshow("Horizontal and vertical",Horizontal_vertical)

# Size of image in bite>>
Size_of_image = image.size
print(Size_of_image)



cv2.waitKey(0)

cv2.destroyAllWindows()