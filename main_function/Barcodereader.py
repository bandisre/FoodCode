from pyzbar.pyzbar import decode 
import cv2
import numpy as np
import time

def barcode_reader_camera():
	cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera
	cap.set(3,640) #width
	cap.set(4,480) #height

	while True:
		myData = 0
		success, img = cap.read()
		for barcode in decode(img):
			myData = barcode.data.decode('utf-8')
			pts = np.array([barcode.polygon], np.int32)
			pts = pts.reshape((-1,1,2))
			cv2.polylines(img,[pts],True,(255,0,0),5)

		cv2.imshow('result',img)
		cv2.waitKey(1) 

		if myData:
			cv2.destroyAllWindows()
			break
	
	return myData

	

if __name__ == '__main__':
	barcode_reader_camera()