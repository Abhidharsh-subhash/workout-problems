class hashtable:
    def __init__(self):
        self.capacity=20
        self.arr=[[] for i in range(self.capacity)]

    def hash(key):
        s=0
        for i in key:
            s+=ord(i)
        return s % 20
    
    def insert(self,key,value):
        hashindex=self.hash(key)
        found=False
        for index,element in enumerate(self.arr[hashindex]):
            if len(element) == 2 and element[0] == key:
                self.arr[hashindex][index]=(key,value)
                found=True
                break
        if found == False:
            self.arr[hashindex].append((key,value))

    def get(self,key):
        hashindex=self.hash(key)
        for element in self.arr[hashindex]:
            if element[0] == key:
                return element[1]
            
    def delete(self,key):
        hashindex=self.hash(key)
        for index,element in enumerate(self.arr[hashindex]):
            if len(element) == 2 and element[0]==key:
                del self.arr[hashindex][index]