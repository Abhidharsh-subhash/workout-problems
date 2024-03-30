# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
from collections import Counter

def canConstruct(ransomNote: str, magazine: str):
    # x={}
    # y={}
    # for i in ransomNote:
    #     if i not in x.keys():
    #         x[i]=1
    #     else:
    #         x[i]+=1
    # for j in magazine:
    #     if j not in y.keys():
    #         y[j]=1
    #     else:
    #         y[j]+=1
    # for key in x.keys():
    #     try:
    #         if y.get(key) < x.get(key):
    #             return False
    #     except:
    #         return False
    # return True
    note=Counter(ransomNote)
    mag=Counter(magazine)
    for key in note.keys():
        if ((mag.get(key) is not None) and (note.get(key) is not None)) :
            if mag.get(key) < note.get(key):
                return False
    return True


ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote,magazine))
