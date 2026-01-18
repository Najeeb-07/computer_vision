import cv2
car_cascade = cv2.CascadeClassifier('cars.xml') 
cap = cv2.VideoCapture('cars.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    cars = car_cascade.detectMultiScale(frame, 1.1, 1)
    for (x,y,w,h) in cars: cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imshow('Cars', frame)
    if cv2.waitKey(1) == ord('q'): break
cap.release()