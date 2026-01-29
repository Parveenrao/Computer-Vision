# Brightness in image ---> overall intensity of an image 

import numpy as np 
import cv2

img = cv2.imread("pexels-kasperphotography-1042423.jpg")

beta = 40 

bright = cv2.add(img , np.ones(img.shape , dtype="uint8") * beta)

cv2.imshow('Original' , img)
cv2.imshow('bright' , bright)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Industry standard

bright2 = cv2.convertScaleAbs(img , alpha=1.0 , beta=beta)

cv2.imshow("Bright" , bright)

cv2.waitKey(0)
cv2.destroyAllWindows()



