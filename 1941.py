# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

from collections import defaultdict


def areOccurrencesEqual(s):
    # count = s.count(s[0])
    # for i in range(1,len(s)):
    #     if s.count(s[i]) != count:
    #         return False
    # return True

    # x={}
    # for i in range(len(s)):
    #     if s[i] not in x.keys():
    #         x[s[i]]=1
    #     else:
    #         x[s[i]]+=1
    # print(x)
    # values=list(x.values())
    # setlist=set(values)
    # if len(setlist) == 1:
    #     return True
    # else:
    #     return False

    # x=[]
    # for i in set(s):
    #     x.append(s.count(i))
    # if len(set(x)) == 1:
    #     return True
    # return False

    d = defaultdict(int)
    print(d)
    for i in s: d[i] += 1
    c = d[s[0]]
    print(d)
    print(c)
    for i in d:
        if d[i] != c: return 0
    return 1


s = "aaabb"
print(areOccurrencesEqual(s))