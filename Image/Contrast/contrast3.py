import cv2

img = cv2.imread("output1.png", cv2.IMREAD_GRAYSCALE)

def update(val):
    alpha = val / 10   # scale: 0.1 → 3.0
    contrast = cv2.convertScaleAbs(img, alpha=alpha, beta=0)
    cv2.imshow("Contrast Control", contrast)

cv2.imshow("Contrast Control", img)
cv2.createTrackbar("Contrast", "Contrast Control", 10, 30, update)

update(10)
cv2.waitKey(0)
cv2.destroyAllWindows()
