#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

from argparse import MetavarTypeHelpFormatter
import json
filename = 'user_settings.json'

myfile = open(filename, mode='w', encoding='utf-8')

user1 = {
    'UserName': "Mike Nigel",
    'Score': 350,
    'Awards': ["OR", "NV", "NY"]
}

user2 = {
    'UserName': "Dave Cool",
    'Score': 336,
    'Awards': ["WI", "TX", "MI"]
}

myusers = []
myusers.append(user1)
myusers.append(user2)


#   #SAVE BY JSON#

json.dump(myusers, myfile)

myfile.close()


#   #LOAD BY JSON#

myfile = open(filename, mode='r', encoding='utf-8')
json_data = json.load(myfile)

for user in json_data:
    print("User name is: " + str(user['UserName']))
    print("User score is: " + str(user['Score']))
    print("User award №1: " + str(user['Awards'][0]))
    print("User award №1: " + str(user['Awards'][1]))
    print("User award №1: " + str(user['Awards'][2]))
    print("----------------------------------------")