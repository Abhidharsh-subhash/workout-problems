# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):
    # result=''
    # for i in range(len(strs[0])):
    #     count=1
    #     for j in range(1,len(strs)):
    #         if result+strs[0][i] in strs[j]:
    #             count+=1
    #     if count == len(strs):
    #         result+=strs[0][i]
    # return result
    # result = ''
    # if len(strs)<=1:
    #     result=''.join(strs)
    #     return result
    # elif len(strs) == 2:
    #     for i in range(len(strs[0])):
    #         if i<=len(strs[1])-1:
    #             if (strs[0][i] == strs[1][i]):
    #                 if i == 0:
    #                     result+=strs[0][i]
    #                 elif strs[0][i-1] in result:
    #                     result+=strs[0][i]
    #     return result
    # else:
    #     for i in range(len(strs[0])):
    #         count=1
    #         for j in range(1,len(strs)):
    #             if len(strs[j])-1>=i:
    #                 if strs[j][i] == strs[0][i]:
    #                     count+=1
    #         if count == 3:
    #             if i == 0:
    #                 result+=strs[0][i]
    #             elif strs[0][i-1] in result:
    #                 result+=strs[0][i]
    #     return result
    result = ''
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return result
        result+=first[i]
    return result

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))