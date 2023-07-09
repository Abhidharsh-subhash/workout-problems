# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

def interpret(command):
    result=''
    for i in range(len(command)):
        if command[i]=='(' and command[i+1]==')':
            result+='o'
        elif command[i]=='(' or command[i]==')':
            continue
        else:
            result+=command[i]
    return result

command = "(al)G(al)()()G"
print(interpret(command))