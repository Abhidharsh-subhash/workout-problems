# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false

# with time complexity O(n^2)
def duplicate(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                return True
    return False

nums = [1,2,3,4]
print(duplicate(nums))

# with time complexity O(n), using set
def duplicate(array):
    seen=set()
    for i in array:
        if i not in set:
            seen.add(i)
        else:
            return True
    return False
