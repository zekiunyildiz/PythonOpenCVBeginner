import cv2
cap = cv2.VideoCapture("fener.mp4")#kendi webcam'ime bağlandım
#cap = cv2.VideoCapture(0)#kendi webcam'ime bağlandım
while True: #sonsuz döngüm
    ret, frame = cap.read() # her kareyi tek tek okudum
    if ret == 0: # video bittiğinde ret 0 olacağı için döngüyü kırmalı.
        break #döngüyü kırdığında break komutu çalışır.


    frame = cv2.flip(frame,1) #Aldıımız görüntüyü ters çeviriyoruz

    cv2.imshow("Fener", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"): #ms kare
        break
cap.release()
cv2.destroyAllWindows()
