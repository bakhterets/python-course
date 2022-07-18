#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

enemy = {
          'loc_x': 70,
          'loc_y': 70,
          'color': 'green',
          'health': 100,
          'name': 'Mudlo'
}

print(enemy)

print("Location X is: " +str(enemy['loc_x']))

print("Location Y is: " +str(enemy['loc_y']))

print("His name is: " + enemy['name'])

enemy["Role"] = 'Bard'

print(enemy)

del enemy['Role']

print(enemy)