import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\Zeki\\Desktop\\Proje Erdinc Uzun\\haarcascade\\frontalface.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\Zeki\\Desktop\\Proje Erdinc Uzun\\haarcascade\\eye.xml")

vid = cv2.VideoCapture("C:\\Users\\Zeki\\Desktop\\Proje Erdinc Uzun\\videos\\pak.mp4")

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame,(480,360))

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,6)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    roi_frame = frame[y:y+h,x:x+w]
    roi_gray = gray[y:y+h,x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    cv2.imshow("Video",frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
