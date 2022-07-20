#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

import sys

filename = 'Lesson_List.txt'

#myfile = open(filename, mode='r', encoding='utf-8')
#
#print(myfile.read())
while True:
    try:
        print('inside TRY')
        myfile = open(filename, mode='r', encoding='utf-8')
    except Exception:
        print('Inside EXCEPT')
        print('## ERROR FOUND! ##')
        print(sys.exc_info()[1])
        filename = input('Enter correct file name!:')

    else:
        print('Inside ELSE')
        print(myfile.read())
        myfile.close()
        sys.exit()
    finally:
        print('Inside FINALLY')

print('===================EOF===================')
