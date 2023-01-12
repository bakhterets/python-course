#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

import importlib
import sys
import argparse
import achievlist

def createParser():
    parser = argparse.ArgumentParser(
        prog = 'recursion programm',
        description = 'This progrom does the recursion'
        )
    subparsers = parser.add_subparsers(dest = 'command',
    title = 'Possible commands',
    description='Commands to be taken as the first parameter of script')

    user_parser = subparsers.add_parser('name_choice')
    user_parser.add_argument('name',choices=['Mike','Slike','Stan','Brave'])
    user_parser.add_argument('age',type=int)

    return parser

def greetings(namespace):

    modulename = namespace.name

    module = importlib.import_module(modulename, package=None)

    achiev_list = module.achievlist

    discovery_list = {"data": []}

    #print("Hi! " + str(person))

