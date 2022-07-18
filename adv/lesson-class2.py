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



myhero1 = SuperHero("Gule", 5, "Dead", 3)
myhero2 = SuperHero("Paladin", 6, "Human", 5)

myhero1.show_hero()
myhero1.move()
myhero1.make_magic()
myhero1.lvl_up()
myhero1.show_hero()

print("\n" + myhero2.name + " turn\n")

myhero2.show_hero()
myhero2.move()
myhero2.make_magic()
myhero2.set_health(60)
myhero2.lvl_up()
myhero2.lvl_up()
myhero2.magic = 500
myhero2.show_hero()