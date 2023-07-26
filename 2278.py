# Input: s = "foobar", letter = "o"
# Output: 33
# Explanation:
# The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.

def percentageLetter(s,letter):
    c=s.count(letter)
    if c != 0 :
        n=len(s)
        return int((c/n)*100)
    return 0

s = "jjjj"
letter = "k"
print(percentageLetter(s,letter))