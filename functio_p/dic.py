# def cube(num):
#     return num+num+num
# result = cube(12)
# print(result)

# def ibad(iop):
#     return iop*iop*iop
# umar = ibad(120)
# print("your result is : ",umar)

# react={
#     "Fan Name  ": "Ik Fan",
#     "Fan Price ": 7888,
#     "Quantity  ": 66,
#     "Quality   ": "Copper"
# }
# print("Fan Name  : ", react["Fan Name  "])
# print("Fan Price : ", react["Fan Price "])
# print("Quantity  : ", react["Quantity  "])
# print("Quality   : ", react["Quality   "])



# Author  Mr.Dr Ibad Ur Rehman 
# skharulation={
#     "name of husband": "Gul Alam Khan",
#     "name of wife": "jeeeeeeee",
#     "name of son": "suroor khan",
#     "name of love": "har waqt sms pi laga rahna",
#     "name of dauter": "yumna shen stargy zama angor"
# }
# print("name of husband : ", skharulation["name of husband"])
# print("name of wife    : ", skharulation["name of wife"])
# print("name of son     : ", skharulation["name of son"])
# print("name of love    : ", skharulation["name of love"])
# print("name of dauter  : ", skharulation["name of dauter"])

def is_sub_string(string: str, sub_string: str) -> bool:
    """
    Paramaters
    ----------
        string
            actual string
        sub_string
            sub string of the actual string
    
    Returns
    -------
        True if sub_string
        False else
    """

    if not isinstance(string, str) and not isinstance(sub_string, str):
        raise ValueError("Both argumets must be of type str")
    
    for i in range(len(string)):
        if string[i:] == sub_string:
            return True
    return False