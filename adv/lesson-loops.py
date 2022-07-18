#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

for x in range(100, 10, -2):
    print("Number x = " + str(x))
    if x == 50:
        break

print("----------EOF----------")

x = 0
while True:
    print(x)
    x = x + 1
    if x == 100:
        break