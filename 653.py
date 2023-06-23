# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

def findMaxAverage(array,k):
    s=sum(array[:k])
    m=s
    for i in range(len(array)-k):
        s+=array[i+k]-array[i]
        m=max(m,s)
    result=m/k
    return result

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))
