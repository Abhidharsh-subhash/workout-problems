# Input: num1 = "11", num2 = "123"
# Output: "134"

import sys


def addStrings(num1,num2):
    #setting the maximum limit for the number of digits when converting integers to strings.
    sys.setrecursionlimit(10000)
    return str(int(num1)+int(num2))

num1 = "11"
num2 = "123"
print(addStrings(num1,num2))