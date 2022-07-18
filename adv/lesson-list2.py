#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

#       0       1     2     3       4
cars = ['bmw','vw','seat','skoda','kada']
#
#for car in cars:
#    print(car.upper())
#
#for x in range(1, 6):
#    print(x)
#
number_list = list(range(0, 10))
print(number_list)

for x in number_list:
    x = x*2
    print(x)

number_list.sort(reverse=True)
print(number_list)

print("Max number is: " + str(max(number_list)))
print("Min number is: " + str(min(number_list)))
print("Sum of list is: " + str(sum(number_list)))

mycars = cars[1:4]
print(mycars)

mycars = cars[-3:-1]
print(mycars)