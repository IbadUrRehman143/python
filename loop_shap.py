row = input("Enter Your First Value")
col = input("Enter Your Second Value")
row= int(row)
col= int(col)
for i in range(row):
    if i == 0 :
     for j  in range(col):
          print("*" , end="")

    if i > 0 and i < row-1 :
       print()
       print("*" , end="")
       for j in range (col-2)  :
          print(" " , end="")
       print("*" , end="")
    if i == row-1 :
       print()
       for j in range (col) :
          print("*" , end="")        



