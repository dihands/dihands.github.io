from PIL import Image
import numpy as np

# Load the image
image_path = "/mnt/data/black-skull-poison-sign-danger-sign-with-skull-warning-icon-of-poison-toxic-chemical-and-electricity-danger-symbol-of-death-vector.jpg"
image = Image.open(image_path)

# Convert image to grayscale
image_gray = image.convert("L")

# Threshold to convert to binary image (0 and 1)
threshold = 128
image_binary = image_gray.point(lambda p: p > threshold and 1)

# Convert to numpy array for easy manipulation
image_array = np.array(image_binary)

# Display the binary image array
image_array
