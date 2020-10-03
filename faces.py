import cv2

face_cascade = cv2.CascadeClassifier('./src/cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                                                      ############## gray holds the black and white version of frame image.           ############
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for(x,y,w,h) in faces:
        print(x,y,w,h)

    color = (255,0,0)  #BGR
    stroke = 2
    end_cord_y = y+h
    end_cord_x = x+w
    cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):                                                          ############## to manual exit the frame.                                        ############
        break

cap.release()
cv2.destroyAllWindows()