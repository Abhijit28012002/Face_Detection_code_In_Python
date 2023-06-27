import cv2
cap=cv2.VideoCapture(0)
while True:
    status,photo=cap.read()
    #photo=cv2.cvtColor(photo,cv2.COLOR_BGR2HLS)
    model=cv2.CascadeClassifier("raw.githubuhaarcascade_frontalface_default.xml")
    myface=model.detectMultiScale(photo)
    x1=myface[0][0]
    y1=myface[0][1]
    x2=myface[0][0]+myface[0][2]
    y2=myface[0][1]+myface[0][3]
    #cv2.rectangle(photo,(x1,y1),(x2,y2),[255,0,0],5)
    photo=photo[y1:y2,x1:x2]
    cv2.imshow("my photo",photo)
    if cv2.waitKey(100)==13:
        break
    
cv2.destroyAllWindows()
cap.release()
