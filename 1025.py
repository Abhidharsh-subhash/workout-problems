# Input: n = 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.

def divisorGame(n):
    i=1
    count=0
    while i<=(n/2):
        if n%i == 0:
            count+=1
            n=n-i
            i=1
        else:
            i+=1
    if count % 2 == 1:
        return True
    else:
        return False
    
n=3
print(divisorGame(n))
