# Contrast ---> differcen between the dark and bright pixel 

import cv2
import numpy as np 

img = cv2.imread("output.png" , cv2.IMREAD_GRAYSCALE)

alpha = 1.8   # contrast factor 

contrast_img = cv2.convertScaleAbs(img , alpha=alpha , beta=0)

cv2.imshow("original_img" , img)
cv2.imshow("Contrast_img" , contrast_img)

cv2.waitKey(0)
cv2.destroyAllWindows()