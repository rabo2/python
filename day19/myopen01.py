import cv2

image = cv2.imread("Image/butterfly.jpg", cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imshow("butterfly", image)

cv2.waitKey(0)
cv2.destroyAllWindows()