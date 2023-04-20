def mergeAlternately(word1, word2):
        result=""
        i=0
        j=0
        l1=len(word1)
        l2=len(word2)
        while (i<l1 and j<l2):
            result+=(word1[i]+word2[j])
            i+=1
            j+=1

        while i<l1:
            result+=word1[i]
            i+=1
        while j<l2:
            result+=word2[j]
            j+=1

        return result


a='abjgvkuvkj'
b='pqrs'
print(mergeAlternately(a,b))