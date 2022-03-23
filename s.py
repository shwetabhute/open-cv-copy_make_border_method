import cv2

# path
path = 'numpy.jpg'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.copyMakeBorder() method
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=0)

# Displaying the image
cv2.imshow(window_name, image)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()

# Displaying the image
cv2.imshow(window_name, image)