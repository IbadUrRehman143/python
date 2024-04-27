fanlist=[]

temp1=input("Enter Your Price Of apple  ")
temp2=input("Enter Your Price Of Mango  ")
temp3=input("Enter your Price Of baffalo")
temp4=input("Enter your Price Of Camale ")
temp5=input("Enter your Price Of banana ")


fanlist.append(temp1)
fanlist.append(temp2)
fanlist.append(temp3)
fanlist.append(temp4)
fanlist.append(temp5)

fanlist[0]=int(fanlist[0])
fanlist[1]=int(fanlist[1])
fanlist[2]=int(fanlist[2])
fanlist[3]=int(fanlist[3])
fanlist[4]=int(fanlist[4])

totalPrice= fanlist[0] + fanlist[1] + fanlist[2] + fanlist[3] + fanlist[4]
if totalPrice > 20000:
    print("Your Bill Is Above 20k : ")
if totalPrice < 20000 :
    print("Your Bill Is Less From 20k : ")
if totalPrice > 20000 :
    print("congragulation You Got Discount 10 : ")
    

print(fanlist)
print(totalPrice)

quantity =[]
temp1 = input("Enter Your Apple Quantity : ")
temp2 = input("Enter Your Apple Quantity : ")
temp3 = input("Enter Your Apple Quantity : ")
temp4 = input("Enter Your Apple Quantity : ")

Price=[
    fanlist[0] * quantity[0], 
    fanlist[1] * quantity[1], 
    fanlist[2] * quantity[2],
    fanlist[3] * quantity[3],
]
listTotalPrice= Price[0] + Price[1] + Price[2] + Price[3]
print(Price)
print(listTotalPrice)
