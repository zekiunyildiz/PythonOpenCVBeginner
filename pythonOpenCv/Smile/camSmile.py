import cv2

vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("C:\\Users\\Zeki\\Desktop\\Proje Erdinc Uzun\\haarcascade\\frontalface.xml")
smile_cascade = cv2.CascadeClassifier("C:\\Users\\Zeki\\Desktop\\Proje Erdinc Uzun\\haarcascade\\smile.xml")

while True:
    ret,frame = vid.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    roi_img = frame[x:x+w,y:y+h]
    roi_gray = gray[x:x+w,y:y+h]
    smiles = smile_cascade.detectMultiScale(roi_gray, 1.5, 5)

    for (ex, ey, ew, eh) in smiles:
        cv2.rectangle(roi_img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)

    cv2.imshow("videos", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
vid.release()
cv2.destroyAllWindows()