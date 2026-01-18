import cv2

# Load the image
img = cv2.imread('house.jpg')

# 1. Scale Bigger (2 times the original size)
bigger = cv2.resize(img, (0, 0), fx=2, fy=2)

# 2. Scale Smaller (0.5 times the original size)
smaller = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Show results
cv2.imshow('Original', img)
cv2.imshow('Bigger', bigger)
cv2.imshow('Smaller', smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()