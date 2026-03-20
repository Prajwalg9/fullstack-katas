import cv2

# Read the image from file
image_path = 'images/forest_image.png'

# Load the image using OpenCV
image = cv2.imread(image_path)

# To check the dimensions of the image
print("Dimensions of image: ",image.shape)

# Resize the image to a new width and height
new_width = 800
new_height = 600
resized_image = cv2.resize(image, (new_width, new_height))

# Display the resized image in a window
cv2.imshow('Resized Forest Image', resized_image)

# Wait for a key press and close the displayed window
cv2.waitKey(0)  # Wait for 3000 milliseconds (3 seconds)

# Destroy all OpenCV windows
cv2.destroyAllWindows()