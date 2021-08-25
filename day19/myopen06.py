import cv2

image = cv2.imread("Image/butterfly.jpg", cv2.COLOR_BGR2GRAY)

image = image[100:900, 300:800].copy()

cv2.imshow("butterfly", image)
cv2.imwrite('Image/myImage.jpg', image)


cv2.waitKey(0)
cv2.destroyAllWindows()