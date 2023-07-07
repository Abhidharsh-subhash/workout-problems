# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

def numJewelsInStones(jewels,stones):
    result=0
    for i in stones:
        if i in jewels:
            result+=1
    return result

jewels = "z"
stones = "ZZ"
print(numJewelsInStones(jewels,stones))