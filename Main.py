import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'Dataset'
images = []
Names = []
lis = os.listdir(path)
print(lis)
for i in lis:
    curImg = cv2.imread(f'{path}/{i}')
    images.append(curImg)
    Names.append(os.path.splitext(i)[0])
print(Names)

def Encondings(images):
    ncodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ncode = face_recognition.face_encodings(img)[0]
        ncodeList.append(ncode)
    return ncodeList

def create():
    now = datetime.now()
    dt = now.strftime('%d-%m-%Y')
    x = open(f'Attendence\{dt}.csv' , 'x')
    with open(f'Attendence\{dt}.csv' , 'w') as a:
        a.writelines('Name, Time')

way = 'Attendence'
files = []
y = os.listdir(way)
#print(y)
now = datetime.now()
today = now.strftime('%d-%m-%Y')

x = f"{today}.csv"
#print(x)

for i in y:
    if x not in y:
        create()
    


def Attendence(name):
    now = datetime.now()
    date = now.strftime('%d-%m-%Y')
    #with open('Attendence\Attendence.csv','r') as f:
        #DataList = f.readlines()   
    with open(f'Attendence\{date}.csv' , 'r+') as t:
        DataList = t.readlines()
        nameList = []
        #print(DataList)
        for line in DataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            time = now.strftime('%H:%M:%S')
            t.writelines(f'\n{name},{time}')
    


knownList = Encondings(images)
#print(len(knownList))
print('Process Completed')

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    imgA = cv2.resize(frame,(0,0),None,0.25,0.25)
    imgA = cv2.cvtColor(imgA, cv2.COLOR_BGR2RGB)
    
    cur_Faces = face_recognition.face_locations(imgA)
    cur_ncode = face_recognition.face_encodings(imgA,cur_Faces)

    for ncodeFace,Loc in zip(cur_ncode,cur_Faces):
        match = face_recognition.compare_faces(knownList, ncodeFace)
        dis = face_recognition.face_distance(knownList, ncodeFace)
        #print(dis)
        matchIndex = np.argmin(dis)

        if match[matchIndex]:
            name = Names[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = Loc
            y1,x2,y2,x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            Attendence(name)

    cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()



    



        

