# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

def defangIPaddr(address):
    result=''
    for i in address:
        if i == '.':
            result+='[.]'
        else:
            result+=i
    return result

address = "1.1.1.1"
print(defangIPaddr(address))
