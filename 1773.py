# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

def countMatches(items,ruleKey,ruleValue):
    count=0
    if ruleKey == 'type':
        index=0
    elif ruleKey == 'color':
        index=1
    else:
        index=2
    for i in items:
        if i[index] == ruleValue:
            count+=1
    return count     

items=[["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(countMatches(items,ruleKey,ruleValue))