numbers = [23, 27, 89, 19, 90]

grater = numbers[0]
less = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > grater:
        grater = numbers[i]
    if numbers[i] < less:
        less = numbers[i]
 
print("Grater number is : ", grater)
print("Less number is : ", less)