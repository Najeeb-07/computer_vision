import cv2

# Load the main image and the logo
img = cv2.imread('house.jpg')
logo = cv2.imread('cat.png')

# Resize logo to fit a small area (e.g., 100x100)
logo = cv2.resize(logo, (100, 100))

# Define the region on the main image to place the logo (top-left)
roi = img[0:100, 0:100]

# Blend the ROI and the logo (0.7 weight for img, 0.3 for logo)
result = cv2.addWeighted(roi, 0.7, logo, 0.3, 0)

# Put the blended part back into the main image
img[0:100, 0:100] = result

cv2.imshow('Watermarked Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()