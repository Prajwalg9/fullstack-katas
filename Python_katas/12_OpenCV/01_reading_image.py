import cv2

# Read the image from file
image_path = 'images/forest_image.png'

# Load the image using OpenCV
image = cv2.imread(image_path)

# Display the image in a window
cv2.imshow('Forest_image', image)

# Wait for a key press and close the displayed window
cv2.waitKey(3000)  # Wait for 3000 milliseconds (3 seconds)

#Destroy all OpenCV windows
cv2.destroyAllWindows()