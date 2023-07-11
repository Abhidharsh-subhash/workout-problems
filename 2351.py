# Input: s = "abccbaacz"
# Output: "c"
# Explanation:
# The letter 'a' appears on the indexes 0, 5 and 6.
# The letter 'b' appears on the indexes 1 and 4.
# The letter 'c' appears on the indexes 2, 3 and 7.
# The letter 'z' appears on the index 8.
# The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

def repeatedCharacter(s):
    # result=''
    # x=float('inf')
    # for i in range(len(s)):
    #     for j in range(i+1,len(s)):
    #         if (s[i] == s[j]) and (j-i < x):
    #             x=j-i
    #             result=s[i]
    # return result
    x=[]
    for i in s:
        if i not in x:
            x.append(i)
        else:
            return i

s = "jkodgypoya"
print(repeatedCharacter(s))   