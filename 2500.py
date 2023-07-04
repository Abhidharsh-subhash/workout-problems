# Input: grid = [[1,2,4],[3,3,1]]
# Output: 8
# Explanation: The diagram above shows the removed values in each step.
# - In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
# - In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
# - In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
# The final answer = 4 + 3 + 1 = 8.

def deleteGreatestValue(grid):
    for i in grid:
        i.sort(reverse=True)
    result=0
    for i in range(len(grid[0])):
        maxval=0
        for j in range(len(grid)):
            maxval=max(grid[j][i],maxval)
        result+=maxval
    return result
grid = [[1,2,4],[3,3,1]]
print(deleteGreatestValue(grid))