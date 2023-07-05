# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

def longestSubarray(nums):
        m=0
        l=len(nums)
        one=True
        for i in range(0,l):
            if nums[i]==0:
                one=False
                left=i-1
                right=i+1
                ones=0
                while left>=0:
                    if nums[left]==1:
                        ones=ones+1
                        left=left-1
                    else:
                        break
                while right<l:
                    if nums[right]==1:
                        ones=ones+1
                        right=right+1
                    else:
                        break
                if ones>m:
                    m=ones
        if one:
            return l-1
        return m


nums=[0,1,1,1,0,1,1,0,1]
print(longestSubarray(nums))