# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

def climbStairs(n):
    prev = 1
    prev2 = 0
    for i in range(1, n+1):
        curi = prev + prev2
        prev2 = prev
        prev = curi
    return prev 

n=2
print(climbStairs(4))