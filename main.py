

list=[1,2,3,4,5]

list_mod=[]

for i in list:
    list_mod.append(i**2)

print(list_mod)


print([i**2 for i in list])

print([i**2 for i in list if i > 3])
