# x = "5"
# y = "10"
# x = int(x)
# y = int(y)

# print(x-y)

a = input("Enter first number: ")
b = input("Enter second number: ")
operator = input("Enter an operator(+, -, *, /): ")
a= int(a)
b = int(b)
result = 0

if operator == "+":
    result = a+b
if operator == "-":
    result = a-b
if operator == "/":
    result = a/b
if operator == "%":
    result = a%b
if operator == "*":
    result = a*b
print("Result", result)