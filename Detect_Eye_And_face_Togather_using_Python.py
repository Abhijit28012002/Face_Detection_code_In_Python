import cv2
face_casecade=cv2.CascadeClassifier("raw.githubuhaarcascade_frontalface_default.xml")
eye_casecade=cv2.CascadeClassifier("haarcascade_eye.xml")

cap=cv2.VideoCapture(0)
while True:
    status,photo=cap.read()
    gray_photo=cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
    faces=face_casecade.detectMultiScale(gray_photo,1.5,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(photo,(x,y),(x+w,y+h),[255,0,0],2)
        crop_gray=gray_photo[y:y+h,x:x+w]
        crop_photo=photo[y:y+h,x:x+w]
        eyes = eye_casecade.detectMultiScale(crop_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(crop_photo,(ex,ey),(ex+ew,ey+eh),[0,255,0],2)
            
    cv2.imshow("my Photo",photo)
    if cv2.waitKey(10)==13:
        break
cv2.destroyAllWindows()
cap.release()
