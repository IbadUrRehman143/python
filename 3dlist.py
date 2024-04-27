Fan1list =[]

tem1=input("Enter Your Fan Name ")
tem2=input("Enter Your Fan Price ")
tem3=input("Enter Your Fan S.no ")

Fan1list.append(tem1)
Fan1list.append(tem2)
Fan1list.append(tem3)

Fan1list[1]=int(Fan1list[1])

print("Fan1list",Fan1list)

Fan2list= []
  
tem1=input("Enter Your Fan Name ")
tem2=input("Enter Your Fan  price ")
tem3=input("Enter Your Fan S.No ")
Fan2list.append(tem1)
Fan2list.append(tem2)
Fan2list.append(tem3)

Fan2list[1]=int(Fan2list[1])

print("Fan2list",Fan2list)


Fan3list=[]

tem1=input("Enter Your Fan Name ")
tem2=input("Enter Your Fan Price ")
tem3=input("Enter Your Fan S.No ")  

Fan3list.append(tem1)
Fan3list.append(tem2)
Fan3list.append(tem3)

Fan3list[1]=int(Fan3list[1])

print("Fan3list",Fan3list)

Fan=[]
Fan.append(Fan1list)
Fan.append(Fan2list)
Fan.append(Fan3list)
print(Fan)
totalPrice= Fan[0][1] + Fan[1][1] + Fan[2][1]
print("Total price Is",totalPrice)

