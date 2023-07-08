# Input: n = 4
# Output: true
# Explantion: 4 has three divisors: 1, 2, and 4.

def isThree(n):
    count=1
    for i in range(1,(n//2)+1):
        if n%i == 0:
            count+=1
    if count == 3:
        return True
    else:
        return False
n=2
print(isThree(n))