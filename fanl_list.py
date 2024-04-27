"""
calculate total price
check quality of each fan
"""

fan1List= []

tem1= input("enter Fan Name ")
tem2= input("enter Fan Price ")
tem3= input("enter Fan S.No ")
fan1List.append(tem1)
fan1List.append(tem2)
fan1List.append(tem3)

print("Fan 1 List",fan1List )



fan2list = []

tem1=input("Enter your product Name ")
tem2=input("Enter your product price ")
tem3=input("Enter your product S.no ")

fan2list.append(tem1)
fan2list.append(tem2) 
fan2list.append(tem3)

print(" Fan 2 List ",fan2list)


fan3list=[]

tem1=input("Enter your product ")
tem2=input("Enter Your product price ")
tem3=input("Enter your Product S.no ")


fan3list.append(tem1)
fan3list.append(tem2)
fan3list.append(tem3)

print(" Fan 3 List ", fan3list)

fan1List[1] = int(fan1List[1])
fan2list[1] = int(fan2list[1])
fan3list[1] = int(fan3list[1])
totalPrice= fan1List[1] + fan2list[1] + fan3list[1]

"""
(total/100)*discount
(1000/100)*10
discountPrice = .......
"""

if totalPrice >20000:
    print("Your Bill is Above From 20K")
if totalPrice <20000:
    print("Your Bill Is Less From 20K")
if totalPrice >20000:
    print("Congragulations You Got Discount 10%")


print("Total Price", totalPrice)
discountedPrice =(totalPrice/100)*10
print(discountedPrice)

totalPrice=totalPrice-discountedPrice
print("Your Discount price is Given Below", totalPrice)


