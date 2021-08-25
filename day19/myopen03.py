import cv2

# image = cv2.imread("Image/rpng.png", 1)
# image = cv2.imread("Image/gpng.png", 1)
image = cv2.imread("Image/bpng.png", 1)
print(image)

cv2.imshow("butterfly", image)

cv2.waitKey(0)
cv2.destroyAllWindows()