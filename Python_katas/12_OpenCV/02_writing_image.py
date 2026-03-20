import cv2

# Read the image from file
image_path = 'images/forest_image.png'

#Write the image to a new file
output_path = 'images/forest_B_and_W.png'

cv2.imwrite(output_path, cv2.imread(image_path,0)) # 0 flag to read the image in grayscale

cv2.destroyAllWindows()