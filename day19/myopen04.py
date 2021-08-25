import cv2

image = cv2.imread("Image/bpng.png", 1)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(image)
print(image_gray)

cv2.imshow("butterfly", image)



cv2.waitKey(0)
cv2.destroyAllWindows()