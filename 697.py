def findShortestSubArray(nums):
        # Initialize variables
        degree = 0
        degree_nums = {}
        left = {}
        right = {}
        shortest = len(nums)
        
        # Traverse through the array
        for i, num in enumerate(nums):
            # Update degree and degree_nums
            if num in degree_nums:
                degree_nums[num] += 1
            else:
                degree_nums[num] = 1
            degree = max(degree, degree_nums[num])
            
            # Update left and right
            if num not in left:
                left[num] = i
            right[num] = i
                
        # Find the shortest subarray with degree
        for num, freq in degree_nums.items():
            if freq == degree:
                shortest = min(shortest, right[num] - left[num] + 1)
        
        # Return the shortest subarray length
        return shortest

array=[1,2,2,3,1,4,2]
print(findShortestSubArray(array))