import cv2
import numpy as np

cap = cv2.VideoCapture(0)


 
ret, frame = cap.read()


cv2.imwrite('cam.png', frame) 
cv2.imshow('cam.png', frame)
cv2.waitKey(0)
cap.release()

image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite('cam1.png', image) 
image = cv2.imread("cam1.png")
image=cv2.line(image, (60, 20), (400, 200),(225,0,255) , 3)
image=cv2.rectangle(image, (60, 20), (400, 200),  (0,0,255), 5)
cv2.imshow('cam1.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()