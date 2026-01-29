# Cropping Image --- A selected part of the image u want to process

import cv2

img = cv2.imread("pexels-kasperphotography-1042423.jpg")

roi = img[100:300, 200:400]

cv2.imshow("original"  , img)
cv2.imshow("Roi" , roi)

cv2.waitKey(0)
cv2.destroyAllWindows()