# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. 
# Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

def destCity(paths):
    x=[]
    result=''
    for i in range(len(paths)):
        for j in range(len(paths[i])):
            if paths[i][j] not in x:
                result=paths[i][j]
                x.append(paths[i][j])
                
     return result

paths = [["A","Z"]]
print(destCity(paths))