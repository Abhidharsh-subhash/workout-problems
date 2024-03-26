def myAtoi(s: str):
    integer = ''
    for i in s:
        if i.isdigit():
            integer += i
    if s[s.index(integer[0])-1] == "-":
        return int('-'+integer)
    return int(integer)


print(myAtoi("words and 987"))
