import cv2
import numpy as np

img = cv2.imread("sorloth.jpg",0)

row, col = img.shape[:2]

M = cv2.getRotationMatrix2D((col/5,row/3),90,1)
dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("DST",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()