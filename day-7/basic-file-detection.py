import os

path = 'C:\\Users\\Раиса Владимировна\\Desktop\\py.txt'

if os.path.exists(path):
    print('this loc exist')
    if os.path.isfile(path):
        print('this is file')
    elif os.path.isdir(path):
        print('this is dir')
else:
    print('this loc doesnt exist')