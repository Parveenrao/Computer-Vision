import cv2


# Read image 

img = cv2.imread("ahuanzuishuai111-tea-10266766_1920.jpg")

# show image


cv2.imshow("My image" , img)

# wait until key press

cv2.waitKey(0)


# destroy all window

cv2.destroyAllWindows()


# Write good code

import cv2

# Read image
img = cv2.imread("photo.jpg")

# Check if image loaded successfully
if img is None:
    print("Error: Could not read image.")
    print("Check:")
    print("1. File name is correct")
    print("2. Image exists in the folder")
    print("3. Path is correct")
else:
    # Display image
    cv2.imshow("My Image", img)

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()