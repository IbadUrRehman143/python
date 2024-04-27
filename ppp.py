fan1list=[]

temp1=input("Enter Your Name ")
temp2=input("Enter Your price ")
temp3=input("Enter Your S.no ")

fan1list.append(temp1)
fan1list.append(temp2)
fan1list.append(temp3)

fan1list[1]=int(fan1list[1])

print("Fan 1 List",fan1list)


fan2list=[]


temp1=input("Enter Your Name ")
temp2=input("Enter Your price ")
temp3=input("Enter Your s.no ")

fan2list.append(temp1)
fan2list.append(temp2)
fan2list.append(temp3)

fan2list[1]=int(fan2list[1])

print("Fan 2 List",fan2list)

fan3list=[]

temp1=input("Enter your Name")
temp2=input("Enter your price")
temp3=input("Enter your S.no")

fan3list[1]=int(fan3list[1])

print("Fan 3 List", fan3list)

fan=[]
fan.append(fan1list)
fan.append(fan2list)
fan.append(fan3list)

print("Fan",fan)

totalprice= fan[0][1] + fan[1][1] + fan[2][1]

print("Total Price", totalprice)