# Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
# Output: [[1,6],[3,9],[4,5]]
# Explanation: 
# The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
# The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
# The item with value = 4 occurs in items1 with weight = 5, total weight = 5.  
# Therefore, we return [[1,6],[3,9],[4,5]].

def mergeSimilarItems(items1,items2):
    result=[]
    for i in range(len(items1)):
        for j in range(len(items2)):
            if items1[i][0] == items2[j][0]:
                x=[items1[i][0],(items1[i][1]+items2[j][1])]
                result.append(x)
                break
    for i in range(len(items1)):
        found=False
        for j in range(len(result)):
            if items1[i][0] == result[j][0]:
                found=True
                break
        if found is False:
            result.append(items1[i])
    for i in range(len(items2)):
        found=False
        for j in range(len(result)):
            if items2[i][0] == result[j][0]:
                found=True
                break
        if found is False:
            result.append(items2[i])
    sorted_array = sorted(result, key=lambda x: x[0])
    return sorted_array
items1 = [[1,1],[3,2],[2,3]]
items2 = [[2,1],[3,2],[1,3]]
print(mergeSimilarItems(items1,items2))