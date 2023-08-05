# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

# For each location indices[i], do both of the following:

# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

 

# Example 1:


# Input: m = 2, n = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.

def oddCells(m,n,indices):
    result=0
    arr=[[0 for i in range(n)] for j in range(m)]
    for i in range(len(indices)):
        for j in range(len(indices[i])):
            x=indices[i][j]
            if j == 0:
                for k in range(len(arr[x])):
                    arr[x][k]+=1
            else:
                for k in range(m):
                    arr[k][x]+=1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] % 2 == 1:
                result+=1
    return result
m = 2 
n = 2
indices = [[1,1],[0,0]]
print(oddCells(m,n,indices))
