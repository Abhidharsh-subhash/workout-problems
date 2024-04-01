# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false

def isHappy(n: int):  
    if n == 1:
        return True  
    if len(str(n))>1:
        x=0
        for i in str(n):
            x+=int(i)*int(i)
        if x == 1:
            return True
        else:
            return isHappy(x)
    return False
    
print(isHappy(1))



