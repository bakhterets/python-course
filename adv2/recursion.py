#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2024    Python course           #
#                                           #
#-------------------------------------------#

def fact(n):
    if n == 0 or n == 1:
        return 1
    return fact(n-1) * n

def fib(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    return fib(x-1) + fib(x-2)

def palin(s):
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    return palin(s[1:-1])

def power(x,n):
    if n == 0:
        return 1
    elif n < 0:
        return 1/power(x,-n)
    elif n%2 == 0:
        return power(x, n//2)*power(x, n//2)
    else:
        return power(x,n-1)*x

d = [1,[53,23,[2234,23423,25235],12],2,[3,4,5,[6,7,8,9,[53,23,12]]]]
def nesting(list_d, level=1):
    print(*list_d, 'nesting level is:', level)
    for i in list_d:
        if type(i) == list:
            nesting(i, level+1)


def main():
    print(fact(4))
    print(fib(20))
    print(palin("hallah"))
    print(power(2,-1))
    nesting(d)

if __name__ == "__main__":
    main()
