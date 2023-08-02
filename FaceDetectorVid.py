import cv2
import numpy as np
from PIL import Image


camera = cv2.VideoCapture(0)
fonts = cv2.FONT_HERSHEY_COMPLEX

while True:
    ret, frame = camera.read()
    height, width, ch = frame.shape

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw bounding boxes around the detected faces and count them
    cnt = 0
    for (x, y, h, w) in faces:
        cnt += 1
        center = int(w/2)+x, int(h/2)+y

        offSet = int(width/3.7)

        if (center[0]-offSet > 0) and (center[0]+offSet < width) and (center[1]-offSet > 0 and center[1] + offSet < height):
            ROI = frame[center[1]-offSet: center[1] +
                        offSet, center[0]-offSet: center[0]+offSet]
            
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display the number of faces detected on the top left of the screen
    cv2.putText(frame, 'Faces detected: {}'.format(cnt), (10, 30), fonts, 1, (0, 255, 0), 2)

    cv2.imshow('image', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows
camera.release()