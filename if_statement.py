# fan = list() # they are the same
fan = []

# temp = input("Enter fan name: ")
# fan.append(temp)
# temp = input("Enter fan Price: ")
# fan.append(temp)
# temp = input("Enter fan S.no: ")
# fan.append(temp)
temp = "apple"
fan.append(temp)
temp = 5000
fan.append(temp)
temp = "#666"
fan.append(temp)

print("Fan name is: ", fan[0])
print("Fan S.no is: ", fan[2])
print("Fan price is: ", fan[1])

# tem=int(fan[1])
# fan[1] = tem
fan[1] = int(fan[1])

if fan[1] > 5000:
    print("Good quality fan. ")
if fan[1] <= 5000: 
    print(" Bad Quality. ")



temp="apple "
fan.append(temp)
temp="5555"
fan.append(temp)
tem=("#666")
fan.apppend(temp)

fan[1]