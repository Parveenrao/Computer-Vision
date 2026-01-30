# COntast on RBG Image 

# we directly not apply contrast on color directly


import cv2
import numpy as np 

img = cv2.imread("output1.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h , s , v = cv2.split(hsv)

v = cv2.convertScaleAbs(v , alpha=2 , beta=0)

hsv_new = cv2.merge([h,s ,v])

result = cv2.cvtColor(hsv_new , cv2.COLOR_HSV2BGR)

cv2.imshow("COntrast_color" , result)

cv2.imshow("Original color" , img)

cv2.waitKey(0)
cv2.destroyAllWindows()