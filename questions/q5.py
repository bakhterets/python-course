#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#


import random

test_list = []
for i in range(1, 101, 1):
    test_list.append(i)

print("Original list is : " + str(test_list) + "\n")

random_num = random.choice(test_list)

print("Random number is: " + str(random_num))