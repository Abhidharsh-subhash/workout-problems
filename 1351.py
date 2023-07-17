# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

def countNegatives(grid):
    result=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 0:
                result+=1
    return result

grid = [[3,2],[1,0]]
print(countNegatives(grid))