#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2022    Python course           #
#                                           #
#-------------------------------------------#

from venv import create
from rich import reconfigure


def create_record(name, phone, address):

    """Create record"""

    record = {
        'name': name,
        'phone': phone,
        'address': address,
    }

    return record

user1 = create_record("Vasya", "+995594865784", "Sartin.St 25")
user2 = create_record("Joja", "+995594334234", "Sartin.St 27")

print(user1)
print(user2)


def give_award(medal, *persons):

    """Give Medals to persons"""
    
    for person in persons:
        print("CHel" + person.title() + " Congrats " + medal)

give_award("Za petuha", "vasya", "petya")
give_award("Za Shlukha", "petya", "alex", "vitalik")