mylist = []

inp = int(input("Input your first integer: "))
mylist.append(inp)

inp = int(input("Input your second integer: "))
mylist.append(inp)

inp = int(input("Input your third integer: "))
mylist.append(inp)

inp = int(input("Input your fourth integer: "))
mylist.append(inp)

print("\nmylist[0] =",mylist[0])
print("mylist[1] =",mylist[1])
print("mylist[2] =",mylist[2])
print("mylist[3] =",mylist[3],"\n")

mylist[0],mylist[3] = mylist[3],mylist[0]

print(mylist)