# list = [1000,900,800,700,600,500,400,300,200,100,0]
# for i in range (len(list)-1):
#     for j in range (i+1,len(list)):
#         if list [i] > list[j]:
#             ali = list[i]
#             list[i] = list[j]
#             list[j] = ali
# print("Hello Your Accending Order list ", "List " ,list)

#2 no logic

# list1 = [88,67,45,34,23]
# list2 = [88,67,45,34,23]

# sublist =[]

# for i in range(len(list1)):
#      sublist.append(list1)
# for i in range(len(list2)):
#      sublist.append(list2)
     
# print(sublist, list1) 

# logic no 3

# list = [1,17,19,4,2,6,13,20]
# largest=list[0]
# smallest=list[0]

# for i in range (1,len(list)):
#     if list [i-1] > largest:
#         largest = list[i]
#     if list [i] < smallest:
#         smallest = list[i]

# print("hello your second largest value ",largest)
# print("hello your second smallest value ",smallest)

# LOGOIC NO 4
# width = int(input("enter your first value of width "))
# hight = int(input("enter your first value of height "))

# C= width*hight

# print("your area is ", C)

# logic no 5

# name =  " ibad Ur Rehman "

# for i in range(name):


fans = [888,999,000,888,666,555]
friends = ["billal","awais","umar","khalil","imran"]

friends.insert(1,"kollal")
friends.append("Ali Niaz khan niaz of Ambar Usa ")
friends.append(fans[0])
friends.remove("bilal")
print(friends)