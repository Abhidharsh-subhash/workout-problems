# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

def restoreString(s,indices):
    result=''
    for i in range(len(indices)):
        result+=s[indices.index(i)] 
    return result

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s,indices))
