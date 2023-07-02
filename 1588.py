# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

def sumOddLengthSubarrays(arr):
    result=0
    n=len(arr)
    for i in arr:
        result+=i
    if n%2 == 1 and n>1:
        result=result*2
    if n>3:
        for i in range(n):
            if i+3<=n:
                for j in range(i,i+3):
                    result+=arr[j]
    return result

arr = [6,9,14,5,3,8,7,12,13,1]
print(sumOddLengthSubarrays(arr))