import cv2
import numpy as np

img = cv2.imread('house.jpg')
rows, cols = img.shape[:2]

# Define 3 source points and 3 destination points
pts1 = np.float32([[50,50], [200,50], [50,200]])
pts2 = np.float32([[10,100], [200,50], [100,250]])

# Calculate Matrix and Apply
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Affine Transformation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()