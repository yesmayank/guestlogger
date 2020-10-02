import cv2

face_cascade = cv2.CascadeClassifier('./src/cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):          # to manual exit the frame.
        break

cap.release()
cv2.destroyAllWindows()