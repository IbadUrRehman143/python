name = ""
age = 0
profession = "" 

def take_person_info():
    global name, age, profession
    name = input("Enter take a name ") 
    age = input(" Enter take a age  ")
    profession = (" Enter Take a profession ")

def print_person_info(name, age, profession):
    print("=",*80)
    print("Name", name)
    print("Age", age)
    print("profession",profession)
    print("=", *80)



def array_sum(listOfNumbers):
     addition= 0
     for i in range(len(listOfNumbers)):
           addition = addition + arr[i]
     return addition

arr = [8, 9, 6, 9, 60]
arr2 = [36, 78, 56, 45, 67]
sum = array_sum(arr)
sum1 = array_sum(arr2)
print(sum)
print(sum1)
