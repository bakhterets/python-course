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
          'name': 'Mudlo',
          'awards': ['Cock', 'Chick'],
          'image': ['image1.jpg','image2.jpg','image3.jpg']
}

all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy.copy())

#for unit in all_enemies:
#    print(unit)

all_enemies[5]['health'] = 30
all_enemies[9]['name'] = 'SuperMudlo'
all_enemies[2]['loc_x'] += 10
all_enemies[2]['loc_y'] += 30

print("-----------------------------")

for unit in all_enemies:
    print(unit)