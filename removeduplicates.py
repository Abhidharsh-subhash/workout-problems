def removeduplicates(array,value):
    i=0
    l=len(array)
    while i<len(array):
        if array[i] == value:
            array.pop(i)
            i+=1
        else:
            i+=1
    n=len(array)
    for i in range(len(array),l):
        array.append('_')
    return n,array
arr=[1,4,7,4,2,6,4]
print(removeduplicates(arr,4))



    # def removeElement(self, nums, val):
    #     i=0
    #     l=len(nums)
    #     while i<len(nums):
    #         if nums[i] == val:
    #             nums.pop(i)
    #             i+=1
    #         else:
    #             i+=1
    #     n=len(nums)
    #     for i in range(len(nums),l):
    #         s='_'
    #         nums.append(s)
    #     return n,nums
