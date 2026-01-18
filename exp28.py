import cv2
import numpy as np

img = cv2.imread('holes_image.png', 0)
kernel = np.ones((5,5), np.uint8)

# Apply Closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Closing', closing)
cv2.waitKey(0)