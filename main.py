from functools import reduce

lst=[2,4,8,16]

print(list(map(lambda n:n**2,lst)))


fil=[1,2,4,5,6,7,8,9,10]

print(list(filter(lambda n:n>5,fil)))

red=[5,10,15,20,25]

def cal(lis):
    sum=0

    for i in lis:
        sum+=i

    return sum

print(cal(red))


#print(list(reduce(lambda i,j:i+j,red)))

print(reduce(lambda i,j:i+j,red))