# Input: original = [1,2,3,4], m = 2, n = 2
# Output: [[1,2],[3,4]]
# Explanation: The constructed 2D array should contain 2 rows and 2 columns.
# The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
# The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

# def construct2DArray(original,m,n):
#     count=0
#     if m==1 and n==1:
#         return []
#     else:
#         if (m*n) == len(original):
#             result = [[None for _ in range(m)] for _ in range(n)]
#             for j in range(n):
#                 for i in range(m):
#                     result[i][j]=original[count]
#                     count+=1
#             return result
# original = [1,2,3]
# m = 1
# n = 3
# print(construct2DArray(original,m,n))

def construct2DArray(original, m, n):
    count = 0
    if m == 1 and n == 1:
        return []
    else:
        if m * n == len(original):
            result = [[None for _ in range(n)] for _ in range(m)]
            for j in range(n):
                for i in range(m):
                    result[i][j] = original[count]
                    count += 1
            return result

original = [1,2]
m = 1
n = 1
print(construct2DArray(original, m, n))




