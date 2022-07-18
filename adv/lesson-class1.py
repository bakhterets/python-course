#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

from hero import *

#-------------------ACTION-------------------#



myhero1 = Hero("Gule", 5, "Dead")
myhero2 = Hero("Paladin", 6, "Human")

myhero1.show_hero()
myhero1.move()
myhero1.lvl_up()
myhero1.show_hero()

print("\n" + myhero2.name + " turn\n")

myhero2.show_hero()
myhero2.move()
myhero2.set_health(60)
myhero2.lvl_up()
myhero2.show_hero()
