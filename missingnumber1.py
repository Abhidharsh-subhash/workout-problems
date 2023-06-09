#1) Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

#2) Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

def missing(array):
    for i in range(len(array)):
        if i not in array:
            return i
        
nums = [9,6,4,2,3,5,7,0,1]
print(missing(nums))