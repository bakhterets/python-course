#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#


from collections import namedtuple

Mushroom = namedtuple('Mushroom', ['name', 'poisonous'])

mushrooms = [Mushroom('Portabello', False), Mushroom('Oyster', False),
             Mushroom('Death Cap', True)]
i = 0

for mushroom in mushrooms:
    i += 1
    name = mushroom.name
    print('%d:"%s"'%(i, name))