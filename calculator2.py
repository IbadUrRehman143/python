
a = input("Enter your firest value")
b = input("Enter your second value")
operator =input("enter an operator (*,-,+,/,%)")

a= int(a)
b= int(b)
Results =0


if operator == "-":
    Results = a-b
if operator == "*":
    Results = a*b
if operator == "/":
    Results = a/b
if operator == "%":
    Results = a%b
if operator =="+":
    Results = a+b


print("Results", Results )
