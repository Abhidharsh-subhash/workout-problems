# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

def largestAltitude(gain):
        curr_alt=0
        max_alt=0
        for i in range(0,len(gain)):
            curr_alt+=gain[i]
            max_alt=max(max_alt,curr_alt)
        return max_alt

gain = [-1,0,3,5,9,12]
print(largestAltitude(gain))