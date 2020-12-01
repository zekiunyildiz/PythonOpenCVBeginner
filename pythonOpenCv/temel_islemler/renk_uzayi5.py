import cv2
img = cv2.imread("sorloth.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("SorlothFirst", img)
cv2.imshow("Sorloth", img_rgb)
cv2.imshow("SorlothHSV", img_hsv)
cv2.imshow("SorlothGRAY", img_gray)


cv2.waitKey(0)
cv2.destroyAllWindows()