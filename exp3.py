import cv2

# Open the web camera
cap = cv2.VideoCapture(0)

print("Press 'f' for Fast Motion, 's' for Slow Motion, 'n' for Normal, 'q' to Quit")

# Default delay (Normal speed)
delay = 30 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Add text to the frame to show current mode
    cv2.putText(frame, f"Delay: {delay}ms", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Webcam Speed Control', frame)

    key = cv2.waitKey(delay) & 0xFF
    
    if key == ord('f'):    # Fast Motion
        delay = 1
    elif key == ord('s'):  # Slow Motion
        delay = 200
    elif key == ord('n'):  # Normal Speed
        delay = 30
    elif key == ord('q'):  # Quit
        break

cap.release()
cv2.destroyAllWindows()