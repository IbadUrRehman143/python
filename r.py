# 
list1=[81,67,94,13,25,55,85,35,9,15,4 ]

list2= []
# for i in range (11):
#     ali = int (input("Enter Your Value "))
#     list1.append(ali)

sum = 0 

for i in range (len(list1)):
    sum = sum + list1[i]
mean = sum / len (list1)

for i in range (11):
    sub = list1[i] - mean
    list2.append(sub)
print(f"sum  Value Is {sum} ")
print(f"Mean Value Is {mean} ")
print(f"The Mean Value  Is {list2}")