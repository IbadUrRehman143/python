name = ""
age = 0
profession = ""

def take_person_info():
    global name, age, profession
    name = input("Enter person name ")
    age = input("Enter person age ")
    profession = input("Enter person profession ")

def print_person_info(name, age, profession):
    print("="*50)
    print("Name:", name)
    print("Age:", age)
    print("Profession:", profession)
    print("="*50)


# take_person_info()
# print_person_info(name, age, profession)

# take_person_info()
# print_person_info(name, age, profession)

def array_sum(listOfNumbers):
    addition = 0
    for i in range(len(listOfNumbers)):
        addition = addition + arr[i]
    # print(addition)
    return addition


arr = [2, 5, 4, 9, 7]
arr2 = [5, 8, 4, 8]
sum = array_sum(arr2)
sum1 = array_sum(arr)
print(sum)
print(sum1)