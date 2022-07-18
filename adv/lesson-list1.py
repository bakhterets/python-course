#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

from operator import truediv


cities = ['New Y','Moscow','New Dehli']

print(cities)
print(len(cities))

print(cities[0].upper())

cities[2] = 'Tula'

print(cities)

cities.append('Kursk')

print(cities)

cities.insert(2, 'Feodos')

print(cities)

del cities[-1]

print(cities)

cities.remove('Tula')

print(cities)

deleted_city = cities.pop()

print("deleted city is: ", deleted_city)

cities.sort(reverse=True)

print(cities, 'reverse')


cities.reverse()

print(cities)
