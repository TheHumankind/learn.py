import os, shutil

path = 'file-deleting.txt'
dir_path = 'file-deleting'

try:
    # os.remove(path)
    # os.rmdir(dir_path)
    shutil.rmtree(dir_path)
except FileNotFoundError:
    print('file to delete isn\'t found')
except PermissionError:
    print('u do not have permission to delete that')
else:
    print('true')
