#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#
import copy


#-------------------------------------------#
some_list = [1, 2, 3]

print(list(filter(lambda x: isinstance(x, int), some_list)))



if type(some_list) is list:
    print("some_list is list")
else:
    print("some_list is not list, this is the: " + type(some_list))


#-------------------------------------------#


print(some_list is copy.deepcopy(some_list))