# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

def diagonalSum(mat):
    if len(mat) == 1:
        return mat[0][0]
    x=0
    y=len(mat[1])-1
    result=0
    for i in mat:
        if x<len(mat) and y>=0:
            if x!=y:
                result+=(i[x]+i[y])
                x+=1
                y-=1
            else:
                result+=i[x]
                x+=1
                y-=1
    return result
mat = [[5]]
print(diagonalSum(mat))
