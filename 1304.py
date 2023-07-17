# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

def sumZero(n):
    if n == 1 or n == 0:
        return [0]
    else:
        result=[]
        if n%2 == 1:
            result.append(0)
            x=(n-1)/2
          return
