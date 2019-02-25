import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	cv2.imshow('frame', frame)

	if cv2.waitKey(20) & 0xFF == ord('q'):
		break


cap.release()
cap.distroyAllWindows()