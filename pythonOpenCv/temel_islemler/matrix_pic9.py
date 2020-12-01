import cv2
import numpy as np

img = cv2.imread("sorloth.jpg")

row,col = img.shape[:2]

M = np.float32([[1,0,-5],[0,1,20]])#siyah örtü

dst = cv2.warpAffine(img,M,(row,col))

cv2.imshow("DST",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()