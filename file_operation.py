with open("example.txt","a") as file:
    for i in range(10):
        file.write(str(i))
        file.write("\n")


with open("example.txt","r") as file:
    for i in file.readline():
        print(i)