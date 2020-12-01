#roi - - > region of interest --> ilgi alanı
import cv2

img = cv2.imread("sorloth.jpg")

#print(img.shape)

roi = img[10:150, 400:500]

cv2.imshow("Parca", roi)
cv2.imshow("Sorloth", img)
cv2.waitKey(0)
cv2.destroyAllWindows()