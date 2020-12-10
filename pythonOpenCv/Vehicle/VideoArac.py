import cv2

vid = cv2.VideoCapture("C:\\Users\\Zeki\\Desktop\\Proje Erdinc Uzun\\videos\\road.mp4")
car_cascade = cv2.CascadeClassifier("C:\\Users\\Zeki\\Desktop\\Proje Erdinc Uzun\\haarcascade\\car_cascade.xml")

while True:
    ret,frame = vid.read()
    frame = cv2.resize(frame,(720,480))

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.5,1)

    for(x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow("video",frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
vid.release()
cv2.destroyAllWindows()