# Input: s = "anagram", t = "nagaram"
# Output: true

from collections import Counter


def isAnagram(s,t):
    # s=sorted(s)
    # t=sorted(t)
    # sCount = Counter(s)
    # tCount = Counter(t)
    # print(sCount)
    # print(tCount)
    # if s == t:
    #     return True
    # else:
    #     return False
    x=Counter(s)
    y=Counter(t)
    print(x,y)
    if x == y:
        return True
    return False

s = "rat"
t = "car"
print(isAnagram(s,t))