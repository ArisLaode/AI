#!/usr/bin/python3

import cv2

def image():

    thresh = 128

    img_grey = cv2.imread('../AI/image/colour.jpg', cv2.IMREAD_GRAYSCALE)
    
    img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

    cv2.imwrite('../AI/image/black-and-white.jpg',img_binary)

    print('Success! Please check your path image')

if __name__ == "__main__":
    image()