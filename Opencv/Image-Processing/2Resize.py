""" 
=> Resize Image Using Opencv

"""

import cv2

img = cv2.imread("ahuanzuishuai111-tea-10266766_1920.jpg")

if img is None:
    print("Image not found")
    exit()

# check dimension

print(img.shape)



# Resize image 

resized = cv2.resize(img , (500 , 300))   # tuple means width and height

print(resized.shape)

cv2.imshow("Original" , img)
cv2.imshow("resized" , resized)

cv2.waitKey(0)

cv2.destroyAllWindows()