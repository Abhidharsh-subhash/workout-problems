# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

def repeating(A):
    # result = []
    # for c in set(A[0]):
    #         count = A[0].count(c)
    #         occurences = 1
    #         for i in range(1,len(A)):
    #             if c in A[i]:
    #                 count = min(count,A[i].count(c))
    #                 occurences += 1
    #             else:
    #                 break
    #         if occurences == len(A):
    #             for i in range(count):
    #                 result.append(c)
                    
    # return result
    count = {}
    for x in A[0]:
        count[x] = count.get(x, 0) + 1
            
    for x in count:
        for i in range(1,len(A)):
            if x in A[i]:
                count[x] = min(count[x], A[i].count(x))
            else:
                count[x] = 0
                break 
    ans = []
    for k,v in count.items():
            ans += v * [k]
    return ans

words = ["cool","lock","cook"]
print(repeating(words))