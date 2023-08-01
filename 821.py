# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
# Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
# The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
# The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
# For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
# The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

def shortestToChar(s,c):
    result = []
    last_occurrence = float('-inf')
    for i in range(len(s)):
        if s[i] == c:
            last_occurrence = i
        result.append(i - last_occurrence)
    
    last_occurrence = float('inf')
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            last_occurrence = i
        result[i] = min(result[i], last_occurrence - i)

    return result
s = "loveleetcode"
c = "e"
print(shortestToChar(s,c))

