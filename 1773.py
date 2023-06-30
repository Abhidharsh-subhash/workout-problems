# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

def countMatches(items,ruleKey,ruleValue):
    count=0
    for i in range(len(items)):
        for j in range(len(items[i])):
            x=items[i][j]
            if ruleKey=='type' and j==1 and ruleValue==x:
                count+=1
        