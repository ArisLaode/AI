#!/usr/bin/python3

import cv2

face_cascade = cv2.CascadeClassifier("../AI/image_face/haarcascade_frontalface_default.xml")

img = cv2.imread('./image_face/messi.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(
    gray_img,
    scaleFactor = 1.5,
    minNeighbors = 5
)

for x, y, w, h in face:
    img = cv2.rectangle(
        img,
        (x,y),
        (x+w, y+h),
        (0, 255, 0),
        3
    )

resized = cv2.resize(img, (800,600))
cv2.imwrite('./image_face/result_messi.jpg', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('Success! Please check path image_face')