"""
sorting 

list --> [5, 9, 4, 7, 1, 3]
accending
list --> [1, 3, 4, 5, 7, 9]
deccending
list --> [9, 7, 5, 4, 3, 1]

"""

numbers = [5, 9, 4, 7, 1, 3]

# print(numbers)

for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            # swaping
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print(numbers)