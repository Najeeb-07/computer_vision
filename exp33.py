import cv2
cap = cv2.VideoCapture('video.mp4')
frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    frames.append(frame)
for f in reversed(frames):
    cv2.imshow('Reverse', f)
    if cv2.waitKey(30) == ord('q'): break
cap.release()