import cv2
import numpy as np
img_filter = cv2.imread("sorloth.jpg")

blur = cv2.blur(img_filter, (11,11))

cv2.imshow("Original", img_filter)
cv2.imshow("blur", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()