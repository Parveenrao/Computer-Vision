# Normlization ---> Mix max Scaling --> Contrast enhancement technique 


import cv2
import numpy as np 
  
img = cv2.imread("output.png" , 0)  # here 0 means grayscale 

# convert to float -- becuase image store as uint8 format and in norlization this format cant store decimal value 

img = img.astype(np.float32)

# find min and max pixel of the image 

I_min = img.min()
I_max = img.max()

# Min-Max Scaling 

norm_img = (img - I_min) / (I_max - I_min)

norm_img = (norm_img * 255).astype(np.uint8)

# Show results
cv2.imshow("Original Image", cv2.imread("output.png", 0))
cv2.imshow("Min-Max Contrast Image", norm_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Inbuilt function ---->                     

norm_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)




