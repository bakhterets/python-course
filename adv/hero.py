#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#
#------------------EXAMPLE------------------#

#-------------------MAIN-------------------#

class Hero():
    
    """Class to create Hero for the Might and Magic"""
    def __init__(self, name, level, race):
    
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    
    def show_hero(self):
        """ print all parameters of this hero """
        description = (self.name + " Level is: " + str(self.level) + " Race is: " +
                       self.race + " Health is: " + str(self.health)).title()
        print(description)

    def lvl_up(self):
        self.level += 1

    def move(self):
        """ Start moving hero """
        print("Hero " + self.name + " started to move")

    def set_health(self, new_health):
        """ set health """
        self.health = new_health


class SuperHero(Hero):

    """Class to create Super Hero with Magic"""

    def __init__(self, name, level, race, magiclevel):
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.__magic = 100

    def make_magic(self):
        
        """Use magic"""

        self.__magic -= 10

    def show_hero(self):
        """ print all parameters of this SuperHero """
        description = (self.name + " Level is: " + str(self.level) + " Race is: " +
                       self.race + " Health is: " + str(self.health) + " Magic level is: " +
                       str(self.magiclevel) + " Amount of mana is: " + str(self.magic)).title()
        print(description)