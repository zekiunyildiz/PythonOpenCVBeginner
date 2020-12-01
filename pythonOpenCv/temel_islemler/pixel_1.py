import cv2
import numpy as np

img = cv2.imread("sorloth.jpg")#oku

dimension = img.shape
print(dimension)#Boyutunu öğren

color = img[150,200]
print("BGR: ",color)#o pixeldeki renk kodları

blue = img[150,200,0]
print("Blue: ", blue)#BGR 0.indekste mavi

img[420, 500, 0] = 250
print("new blue:", img[420, 500, 0])#img'nin 0. indeksi 250 yaptık

blue1 = img.item(150,200,0)#Blue1'i gösteriyoruz.
print("Blue1:", blue1)

img.itemset((150,200,0), 172)
print("New Blue1:", img[150,200,0])

cv2.imshow("sorloth", img)
cv2.waitKey(0)
cv2.destroyAllWindows()