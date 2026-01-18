import cv2

# Load the image
img = cv2.imread('house.jpg')

if img is None:
    print("Error: house.jpg not found.")
else:
    # 1. Rotate Clockwise (90 degrees)
    clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # 2. Rotate Counter-Clockwise (90 degrees)
    counter_clockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display Results
    cv2.imshow('Original', img)
    cv2.imshow('Clockwise', clockwise)
    cv2.imshow('Counter Clockwise', counter_clockwise)

    cv2.waitKey(0)
    cv2.destroyAllWindows()