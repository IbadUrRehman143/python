name=input("Please Enter A Count Number  ")

name=int(name)

Count=0 

while (name != 0):
    name= int(name/10)
    Count= Count+1


print("Your Count Number Is",Count)

