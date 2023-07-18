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
            x=(n-1)//2
            for i in range(x):
                a=i+1
                result.append(a)
                result.append(a*(-1))
        else:
            x=n//2
            for i in range(x):
                a=i+1
                result.append(a)
                result.append(a*(-1))
        return result
n=5
print(sumZero(n))

#simple solution

# l,rem=n//2,n%2
# if rem != 0:ans=[0]
# else: ans=[]
# for i in range(l+1):
#     ans.append(i)
#     ans.append(-1)
# return ans