# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

import collections


def hasGroupsSizeX(deck):
    count = collections.Counter(deck)
    print(count)

deck = [1,1,2,2,2,2]
print(hasGroupsSizeX(deck))