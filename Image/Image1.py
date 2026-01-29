# Read an image

import numpy as np
import cv2

img = cv2.imread("D:\Computer Vision\Image\pexels-kasperphotography-1042423.jpg")

print(type(img))
print(img.shape)


# correct way to read an image 

imag2 = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

