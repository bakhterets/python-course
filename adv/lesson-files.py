#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

import os

path = os.getcwd()
ifilename = '/passwords.txt'
ofilename = '/weakpasswords.txt'
inputfile = (path + ifilename)
outputfile = (path + ofilename)
pwd_weakcomb = ['9P','9C','9A']

#with open(inputfile, mode='r', encoding='utf-8') as file:
#    data = file.read()
#
#    print(data)
#
#    #for line in data:
#    #    print("Password is: " + line)

myfile1 = open(inputfile, mode='r', encoding='utf-8')
myfile2 = open(outputfile, mode='w', encoding='utf-8')

'''
for num, line in enumerate(myfile1, 1):
    if pwd_weakcomb in line:
        print('Line №: ' + str(num) + ' : ' + line.strip())
'''

for num, line in enumerate(myfile1, 1):
    for comb in pwd_weakcomb:
        if comb in line:
            print('Line №: ' + str(num) + ' : ' + line.strip())
            myfile2.write('Line №: ' + str(num) +' :: ' + 'Found password: ' + line)

myfile1.close()
myfile2.close()
