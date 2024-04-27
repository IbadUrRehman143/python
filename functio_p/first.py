import time
# from time import sleep

def sleep(n):
    print(n)

def is_even(num):
    if (num % 2 == 0 ):
        return "Even"
    else:
        return "Odd"


def print_lst(list):
    print(end='[')
    for elm in list:
        time.sleep(1)
        print(elm, end=", ", flush=True)
    print(end=']')
num=24
results = is_even(num)
print("number is ", results)


NUM1 = 5
NUM2 = 2
NUM3 = 1
NUM4 = 8
NUM5 = 3
NUM6 = 9

