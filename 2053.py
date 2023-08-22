# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned.

def kthDistinct(arr,k):
    x=''
    count=0
    for i in arr:
        if arr.count(i) == 1:
            count+=1
            x=i
        if count == k:
            return x
    return ("")
        
arr = ["d","b","c","b","c","a"]
k = 2
print(kthDistinct(arr,k))