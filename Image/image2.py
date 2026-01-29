# Comvert image to grayscale 

import cv2

img = cv2.imread("pexels-kasperphotography-1042423.jpg")

Gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale" , Gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(Gray_img)

