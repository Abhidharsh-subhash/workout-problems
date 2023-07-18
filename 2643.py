# Input: mat = [[0,1],[1,0]]
# Output: [0,1]
# Explanation: Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of ones (1). So, the answer is [0,1]. 

def rowAndMaximumOnes(mat):
    result=[]
    index=0
    count=0
    # for i in range(len(mat)):
    #     x=0
    #     for j in range(len(mat[i])):
    #         if mat[i][j] == 1:
    #             x+=1
    #     if x>count:
    #         count=x
    #         index=i
    # result.append(index)
    # result.append(count)
    # return result
    for i in range(len(mat)):
        x=mat[i].count(1)
        if x > count:
            count=x
            index=i
    result.append(index)
    result.append(count)
    return result
mat = [[0,1],[1,0]]
print(rowAndMaximumOnes(mat))
