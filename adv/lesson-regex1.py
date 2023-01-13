#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.1 2023    Python course           #
#                                           #
#-------------------------------------------#

import re

mytext = '"OtherLinkTechnology":  "null"' \
         '"OtherNetworkPortType":  "null"' \
         '"PermanentAddress":  "4C034F1100D9"' \
         '"PortNumber":  "0"' \
         '"SupportedMaximumTransmissionUnit":  "null"' \
         '"AdminLocked":  "false"' \
         '"ComponentID":  "BTH\MS_BTHPAN"' \
         '"ConnectorPresent":  "false"' \
         '"DeviceName":  "\\Device\\{0D0EE476-60BE-46B9-8F66-5F3343527AB1}"' \
         '"DeviceWakeUpEnable":  "false"' \
         '"DriverDate":  "2006-06-21"' \
         '"DriverDateData":  "127953216000000000"' \
         '"DriverDescription":  "Bluetooth Device (Personal Area Network)"' \
         '"DriverMajorNdisVersion":  "6"' \
         '"DriverMinorNdisVersion":  "30"' \
         '"DriverName":  "\\SystemRoot\\System32\\drivers\\bthpan.sys"' \
         '"DriverProvider":  "Microsoft"' \
         '"DriverVersionString":  "10.0.19041.1"' \
         '"EndPointInterface":  "false"' \
         '"HardwareInterface":  "false"' \
         '"Hidden":  "false"'

"""
\d  = Any digit 0-9
\D  = Any non digit
\w  = Any alphabet symbol [A-Z a-z]
\W  = Any nin alphabet symbol
\s  = breakspace
\S  = non breakspace

"""

textlookfor = r"\w+\.\w+"
allresults = re.findall(textlookfor, mytext)

print(allresults)


link = "https://www.amalgama-lab.com/songs/b/bring_me_the_horizon/ludens.html"
#pattern = '(?:^.*\/)([^\/]+)(?:\.html)'

result = re.search(r"(?:^.*\/)([^\/]+)(?:\.html)", link)

print(result.group(1))


#if result:
#    print("ok")
#    print(result)
#else:
#    print("ne ok")
