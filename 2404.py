# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.

def mostFrequentEven(nums):
    element=0
    occ=0
    for i in range(len(nums)):
        count=0
        if nums[i]%2 == 0:
            count+=1
            for j in range(i+1,len(nums)):
                if nums[j] == nums[i]:
                    count+=1
            if count >= occ:
                

    return element

nums = [0,1,2,2,4,4,1]
print(mostFrequentEven(nums))
            


