import cv2
import numpy as np
import face_recognition

imgMes = face_recognition.load_image_file('Messi.jpg')
imgMes = cv2.cvtColor(imgMes, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

loc = face_recognition.face_locations(imgMes)[0]
ncode1 = face_recognition.face_encodings(imgMes)[0]
cv2.rectangle(imgMes, (loc[3],loc[0]), (loc[1],loc[2]), (255,0,255),2)

loc = face_recognition.face_locations(imgTest)[0]
ncode2 = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (loc[3],loc[0]), (loc[1],loc[2]), (255,0,255),2)

results = face_recognition.compare_faces([ncode1],ncode2)
dis = face_recognition.face_distance([ncode1],ncode2)
print(results, dis)
cv2.putText(imgTest,f'{results} {round(dis[0],2)}', (50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow("Messi",imgMes)
cv2.imshow("Test",imgTest)
cv2.waitKey(0)
