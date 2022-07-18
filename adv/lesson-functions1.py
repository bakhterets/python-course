#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

def summa(x,y):
    return x+y

def factorial(x):
    answer = 1
    for i in range(1, x+1):
        answer = answer * i
    return answer

x = summa(33, 22)

print(x)

for i in range(1,10):
    print(str(i) + "!\t = " + str(factorial(i)))