import os

source = 'file-moving.txt'
destination = 'C:\\Users\\Раиса Владимировна\\PycharmProjects\\learn-py\\day-8\\file-moving\\file-moving.txt'

try:
    if os.path.exists(destination):
        print('file moved already')
    else:
        os.replace(source, destination)
        print('file moved')
except FileNotFoundError:
    print('file or dir not found')