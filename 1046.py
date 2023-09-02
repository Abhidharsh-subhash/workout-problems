# Input:    
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

def lastStoneWeight(stones):
        stones.sort()
        while stones:
            s1=stones.pop()
            if not stones:
                return s1
            else:
                s2=stones.pop()
                if s1 > s2:
                    stones.append(s1-s2)
                    stones.sort()
        return 0

stones = [1]
print(lastStoneWeight(stones))