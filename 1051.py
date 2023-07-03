# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

def heightChecker(heights):
    org=[]
    count=0
    for i in heights:
        org.append(i)
    n=heights.sort()
    for i in range(len(org)):
        if org[i] != heights[i]:
            count+=1
    return count

heights = [5,1,2,3,4]
print(heightChecker(heights))