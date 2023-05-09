# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# Example 3:
# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.

def lucky(arrary):
    n=-1
    c=0
    for i in range(len(arrary)):
        count=0
        for j in range(len(arrary)):
            if arrary[i] == arrary[j]:
                count+=1
        if arrary[i] == count and arrary[i] > n:
            n=arrary[i]
            c=count
    return n

arr=[2,2,2,3,3]
print(lucky(arr))
