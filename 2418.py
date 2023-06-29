# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.

def sortPeople(names,heights):
    for i in range(len(heights)):
        for j in range(i+1,len(heights)):
            if heights[i]<heights[j]:
                heights[i],heights[j]=heights[j],heights[i]
                names[i],names[j]=names[j],names[i]
    return names
names = ["Alice","bob","Bob"]
heights = [155,185,150]
print(sortPeople(names,heights))