# Input: x = 123
# Output: 321

def reverse(x):
    if x<0:
        n=str(x)[1:]
        return int('-'+n[::-1])
    else:
        n=str(x)
        return int(n[::-1])

x = 123
print(reverse(x))