import time

our_string = "racecar race car"


def palindrome(x):
    start = time.time()
    x = x.strip().replace(" ", "")
    print(x)
    length = len(x)
    left = 0
    right = length - 1
    while left <= right:
        if str(x[left]) != str(x[right]):
            end = time.time()
            print(end - start)
            return False
        left += 1
        right -= 1
    end = time.time()
    print(end - start)
    return True


print(palindrome(our_string))
