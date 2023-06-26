import cv2
cap=cv2.VideoCapture(0)
while True:
    status,photo=cap.read()
    model=cv2.CascadeClassifier("raw.githubuhaarcascade_frontalface_default.xml")
    myface=model.detectMultiScale(photo)
    x1=myface[0][0]
    y1=myface[0][1]
    x2=myface[0][0]+myface[0][2]
    y2=myface[0][1]+myface[0][3]
    cv2.rectangle(photo,(x1,y1),(x2,y2),[255,0,0],5)
    myphoto=photo[x1:x2,y1:y2]
    cv2.imshow("my photo",myphoto)
    if cv2.waitKey(100)==13:
        break
    
cv2.destroyAllWindows()
cap.release()
