# -------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2024    Python course           #
#                                           #
# -------------------------------------------#

string_1 = "This is string 1"
string_1_es = "Esta es la línea 1"

print(string_1)

print(id(string_1))  # String object ID

print(string_1.upper())

print((string_1.upper().capitalize()))

print(string_1.find("is", 0, 11))  # 2

print(string_1.rfind("is", 0, 11))  # 5

print(string_1.index("t", 2, 11))  # 9

print(string_1[9])

print(string_1.replace("his", "hese"))

print(string_1 + " = " + string_1_es)

print((string_1 * 2))

print('{}, {}, {}'.format('x', 'y', 'z'))
