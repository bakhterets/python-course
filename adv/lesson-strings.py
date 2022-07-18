#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

mystring = 'bla bla bla'

name = 'Ilia Bakh'

print(name.title())
print(name.upper())
print(name.lower())

print('privet stroka nomer1\nprivet stroka nomer2\n\nstroka n3')
print('Messages:\n\tMessage1\n\tMessage2\n\tMessage3\nEND')
print('lower name:' + name.lower())
print("#-------------------------------------------#")
a = ".... ded maksim ...."
print(a.rstrip())
print(a.lstrip())
print(a.strip())
print(a.strip("."))
b = a.strip(".")
b = b.strip()
b = b.title()
print(b)