import cv2
import numpy as numpy

faceDetect = cv2.CascadeClassifier("../AI/image_face/haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceDetect.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if (cv2.waitKey(1) == ord('q')):
        break

camera.release()
cv2.destroyAllWindows()