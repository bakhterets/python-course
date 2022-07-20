#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#


import collections

Mushroom = collections.namedtuple('Mushroom', ['name', 'poisonous'])

class MushroomsBusket:

    def __init__(self):

        self._mushrooms = [Mushroom('Oyster', False), Mushroom('Portobello', False)]

mushroom_basket = MushroomsBusket()
print(len(mushroom_basket))