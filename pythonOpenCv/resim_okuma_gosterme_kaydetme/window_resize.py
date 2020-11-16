import cv2
cv2.namedWindow("Sorloth")
img = cv2.imread("sorloth.jpg")


img = cv2.resize(img, (640,480))

cv2.imshow("Sorloth", img)
cv2.waitKey(0)
cv2.destroyAllWindows()