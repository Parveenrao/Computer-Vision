# Resize image

import cv2

img = cv2.imread("pexels-kasperphotography-1042423.jpg")

resized = cv2.resize(img, (300, 200))  # (width, height)

cv2.imshow("Original", img)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
