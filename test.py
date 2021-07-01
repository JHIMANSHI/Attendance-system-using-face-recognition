import os
from datetime import datetime

def xyz(name):
    now = datetime.now()
    date = now.strftime('%d-%m-%Y') 
    with open(f'Attendence\{date}.csv' , 'r+') as t:
        read = t.readlines()
        print(read)
        lis = []
        for line in read:
            x = line.split(',')
            lis.append(x[0])
        print(lis)
        if name in lis:
            time = now.strftime('%H:%M:%S')
            t.write(f'{time}')
xyz(name)
    
        

