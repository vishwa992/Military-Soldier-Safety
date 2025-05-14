import cv2
import numpy as np
import os

# Load image with safety check
image_path = 'battlefield.png'
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file '{image_path}' not found.")

image = cv2.imread(image_path)
if image is None:
    raise ValueError("Failed to load image. Make sure the path is correct and the file is a valid image.")

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define red ranges
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Create red masks
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = mask1 + mask2

# Count red pixels
red_pixels = cv2.countNonZero(red_mask)

# Decide status
if red_pixels > 5000:
    text = "Danger Zone Detected!"
    color = (0, 0, 255)  # Red
else:
    text = "Safe Area"
    color = (0, 255, 0)  # Green

# Annotate and save or show
cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

# Save instead of show if in headless environment
cv2.imwrite("result.png", image)
print(f"{text} (Red pixels: {red_pixels}) - Result saved as 'result.png'")