# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

def lefrigdiff(array):
    n=len(array)
    leftsum=[0]*n
    rightusm=[0]*n
    result=[]

    leftsum[0]=0
    for i in range(1,n):
        leftsum[i]=leftsum[i-1]+array[i-1]
    rightusm[n-1]=0
    for i in range(n-2,-1,-1):
        rightusm[i]=rightusm[i+1]+array[i+1]
    for i in range(0,n):
        x=abs(leftsum[i]-rightusm[i])
        result.append(x)
    return result

array=[10,4,8,3]
print(lefrigdiff(array))