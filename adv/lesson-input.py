#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

#name = input("Please enter your name: \n")
#
#print("Hi!"+ name)
#
#num1 = input("Enter X: ")
#
#num2 = input("Enter Y: ")
#
#summ = int(num1) + int(num2)
#print(summ)


#message = ""
#
#while True:
#    message = input("Enter the password: \n")
#    if message == 'secret':
#        break
#        print(message +" is wrong password!")
#
#
#print("Password was: " + message)

mylist = []
msg = ""

while msg != 'stop'.upper():
    msg = input("Enter new item, and 'STOP' to finigsh ")
    mylist.append(msg)

print(mylist)