#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2024    Python course           #
#                                           #
#-------------------------------------------#
from achievlist import dict_users


users = dict_users

def first_func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

def main():
    first_func(**users)

if __name__ == "__main__":
    main()
