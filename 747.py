# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.

def dominantIndex(array):
    high=max(array)
    ind=array.index(high)
    result=0
    for i in range(len(array)):
        if i!=ind:
            n=array[i]*2
            if high>=n:
                result=ind
            else:
                result=-1
                break
    return result


nums = [1,2,3,4]
print(dominantIndex(nums))