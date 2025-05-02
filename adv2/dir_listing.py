import os

path = '/home/ibakhter/dev/python-course'

def dir_trvsl(path, name, level=1):
    #print('level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if i == name:
            print('FILE FOUND', path+'/'+name)
            pass
        if os.path.isdir(path+'/'+i):
            #print('deep in:', path+'/'+i)
            dir_trvsl(path+'/'+i, name, level+1)
            #print('return to:', path)
            


dir_trvsl(path, 'kwargs.py')
