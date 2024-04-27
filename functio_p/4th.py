def is_allowed(age):
    if age >=18:
        return "He/she is  older than 18 "
    else :
        return " he/she is not older than 18 "
user_age=int(input("enter your age: "))
result= is_allowed(user_age)
print(result)