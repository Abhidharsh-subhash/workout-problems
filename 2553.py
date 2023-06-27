# Input: nums = [13,25,83,77]
# Output: [1,3,2,5,8,3,7,7]
# Explanation: 
# - The separation of 13 is [1,3].
# - The separation of 25 is [2,5].
# - The separation of 83 is [8,3].
# - The separation of 77 is [7,7].
# answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.

def separateDigits(array):
    result=[]
    for i in array:
        n=str(i)
        for j in n:
            k=int(j)
            result.append(k)
    return result 

nums=[7,1,3,9]
print(separateDigits(nums))