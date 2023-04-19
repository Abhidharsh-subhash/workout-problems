def lengthOfLastWord(s):
        l,n=0,0
        s+=' '
        for i in range(len(s)):
            if s[i]!=' ':
                n+=1
            else:
                if n>0:
                    l=n   
                n=0
        return l



print(lengthOfLastWord('hello world '))