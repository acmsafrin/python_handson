file=open("example.txt","w")

for i in range(10):
    file.write(str(i))
    file.write("\n")

file.close()