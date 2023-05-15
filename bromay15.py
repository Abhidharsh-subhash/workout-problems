#to find the average of an array by avoiding the min and max value from the array

def average(salary):
    min=float('inf')
    max=0
    s=0
    for i in salary:
        if i<min:
            min=i
        if i>max:
            max=i
    for i in salary:
        if i!=min and i!=max:
            s+=i
    d=len(salary)-2
    return (s/d)

salary=[1000,2000,3000]
print(average(salary))
