import cv2

vid = cv2.VideoCapture("C:\\Users\\Zeki\\Desktop\\Proje Erdinc Uzun\\videos\\body.mp4")
body_cascade = cv2.CascadeClassifier("C:\\Users\\Zeki\\Desktop\\Proje Erdinc Uzun\\haarcascade\\fullbody.xml")

while True:
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bodies = body_cascade.detectMultiScale(gray,1.1,1)

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    cv2.imshow("video",frame)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()