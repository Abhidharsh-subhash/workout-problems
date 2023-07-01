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
    for i in range(n):
        for j in range(i, n):
            subarray = arr[i:j+1]
            length = len(subarray)
            if length % 2 == 1 and length >= 3:
                result += sum(subarray)
    
    return result

arr = [6,9,14,5,3,8,7,12,13,1]
print(sumOddLengthSubarrays(arr))