#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

import sys
import os

print('Hello!!')
x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "--help" or "-h":
        print("Help requested")
        print("Usage of this program is: python.exe myfile.py $argv1 $argv2")
    print("Arguments entered: " + str(sys.argv[1:]))
else:
    print("No arguments are given")

os.system("ls > listdir.txt")
sys.exit(5)